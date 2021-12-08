import bpy
from bpy.types import Operator
from bpy.props import StringProperty, IntProperty, BoolProperty
from stored_views_advanced.preferences.helper import get_preferences
from .constant import ICONS, SETTINGS_TYPES, TYPE_STORING


class SVA_OT_init_stores(Operator):
    bl_label = "Initialize"
    bl_idname = "sva.init_stores"

    def execute(self, context):
        stores = context.scene.sva.stores
        if not stores:  # Init stores
            for store_name_default in list(TYPE_STORING) + ["global"]:
                new = stores.add()
                new.name = store_name_default
        return {"FINISHED"}


class SVA_OT_add_entry(Operator):
    bl_label = "Add Entry"
    bl_idname = "sva.add_entry"

    store: StringProperty(default="global")
    name: StringProperty()

    def execute(self, context):
        store = context.scene.sva.get(self.store)
        if store.name == "":  # Init store name. Should only be called once
            store.name = self.store

        new = store.add()
        new.name = f"View {len(store)}" if self.name == "" else self.name
        if hasattr(context, self.store):
            current_item = getattr(context, self.store)
            if current_item:
                new.identifier.set(current_item)

        prefs = get_preferences(context).defaults
        sync_settings = new.sync_settings
        for attr in SETTINGS_TYPES:
            setattr(sync_settings, attr, getattr(prefs, attr))

        bpy.ops.sva.store_entry(store=self.store, index=len(store) - 1, is_storing=True)

        return {"FINISHED"}


class SVA_OT_remove_entry(Operator):
    bl_label = "Remove Entry"
    bl_idname = "sva.remove_entry"

    store: StringProperty(default="global")
    index: IntProperty(default=-1)

    def execute(self, context):
        context.scene.sva.get(self.store).remove(self.index)
        return {"FINISHED"}


class SVA_OT_store_entry(Operator):
    bl_label = "Store Entry"
    bl_idname = "sva.store_entry"

    store: StringProperty()
    index: IntProperty(default=-1)
    is_storing: BoolProperty()

    def execute(self, context):
        store = context.scene.sva.get(self.store)
        entry = store.get(self.index)
        sync_settings = entry.sync_settings
        stored_props = entry.stored_props

        if self.is_storing:
            for attr in SETTINGS_TYPES:
                if not getattr(sync_settings, attr):
                    continue
                settings = getattr(entry, attr, None)
                if hasattr(settings, "init"):
                    settings.init()
                try:
                    exec(f"bpy.ops.sva.{attr}_store_settings(store=self.store, index=self.index, is_storing=True)")
                except TypeError:
                    exec(f"bpy.ops.sva.{attr}_store_settings(store=self.store, index=self.index)")

                setattr(stored_props, attr, True)
        else:
            for attr in SETTINGS_TYPES:
                if getattr(sync_settings, attr) and getattr(stored_props, attr):
                    try:
                        exec(f"bpy.ops.sva.{attr}_store_settings(store=self.store, index=self.index, is_storing=False)")
                    except TypeError:
                        exec(f"bpy.ops.sva.{attr}_restore_settings(store=self.store, index=self.index)")

        return {"FINISHED"}


class SVA_OT_store_entry_sync_settings(Operator):
    bl_label = "Synchronization Settings"
    bl_idname = "sva.store_entry_sync_settings"
    bl_options = {"REGISTER", "UNDO"}

    store: StringProperty()
    index: IntProperty()

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        return {"FINISHED"}

    def draw(self, context):
        layout = self.layout
        store = context.scene.sva.get(self.store)

        sync = layout.row(align=True)
        sync_settings = store.get(self.index).sync_settings
        for e in SETTINGS_TYPES:
            sync.prop(sync_settings, e, text="", icon=ICONS.get(e, "BLANK1"))
