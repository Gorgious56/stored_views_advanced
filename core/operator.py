import bpy
from stored_views_advanced.preferences.helper import get_preferences


class SVA_OT_add_entry(bpy.types.Operator):
    bl_label = "Add Entry"
    bl_idname = "sva.add_entry"

    container: bpy.props.StringProperty(default="global")
    name: bpy.props.StringProperty()

    def execute(self, context):
        sva_props = context.scene.sva.get_store(self.container)
        if sva_props.name == "":
            sva_props.name = self.container
        new = sva_props.add()
        new.name = f"View {len(sva_props)}" if self.name == "" else self.name

        prefs = get_preferences(context).settings
        sync_settings = new.sync_settings
        for attr in new.SETTINGS_TYPES:
            setattr(sync_settings, attr, getattr(prefs, f"sync_{attr}"))

        bpy.ops.sva.store_entry(container=self.container, index=len(sva_props) - 1)

        return {"FINISHED"}


class SVA_OT_remove_entry(bpy.types.Operator):
    bl_label = "Remove Entry"
    bl_idname = "sva.remove_entry"

    container: bpy.props.StringProperty(default="global")
    index: bpy.props.IntProperty(default=-1)

    def execute(self, context):
        context.scene.sva.get_store(self.container).remove(self.index)
        return {"FINISHED"}


class SVA_OT_restore_entry(bpy.types.Operator):
    bl_label = "Restore Entry"
    bl_idname = "sva.restore_entry"

    container: bpy.props.StringProperty()
    index: bpy.props.IntProperty()

    def execute(self, context):
        entry = context.scene.sva.get_store(self.container).get(self.index)
        sync_settings = entry.sync_settings
        stored_props = entry.stored_props
        for attr in entry.SETTINGS_TYPES:
            if getattr(sync_settings, attr) and getattr(stored_props, attr):
                exec(f"bpy.ops.sva.{attr}_restore_settings(container=self.container, index=self.index)")
        return {"FINISHED"}


class SVA_OT_store_entry(bpy.types.Operator):
    bl_label = "Store Entry"
    bl_idname = "sva.store_entry"

    container: bpy.props.StringProperty()
    index: bpy.props.IntProperty()

    def execute(self, context):
        entry = context.scene.sva.get_store(self.container).get(self.index)
        sync_settings = entry.sync_settings
        stored_props = entry.stored_props
        for attr in entry.SETTINGS_TYPES:
            if getattr(sync_settings, attr):
                exec(f"bpy.ops.sva.{attr}_store_settings(container=self.container, index=self.index)")
                setattr(stored_props, attr, True)
        return {"FINISHED"}


class SVA_OT_store_entry_sync_settings(bpy.types.Operator):
    bl_label = "Synchronization Settings"
    bl_idname = "sva.store_entry_sync_settings"
    bl_options = {"REGISTER", "UNDO"}

    container: bpy.props.StringProperty()
    index: bpy.props.IntProperty()

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        return {"FINISHED"}

    def draw(self, context):
        layout = self.layout
        store = context.scene.sva.get_store(self.container)

        sync = layout.row(align=True)
        sync_settings = store.get(self.index).sync_settings
        sync.prop(sync_settings, "outliner", text="", icon="OUTLINER")
        sync.prop(sync_settings, "objects", text="", icon="OBJECT_DATAMODE")
        sync.prop(sync_settings, "view_layers", text="", icon="RENDERLAYERS")
        sync.prop(sync_settings, "collections", text="", icon="OUTLINER_COLLECTION")
        sync.prop(sync_settings, "viewport", text="", icon="VIEW3D")
        sync.prop(sync_settings, "shading", text="", icon="SHADING_RENDERED")
        sync.prop(sync_settings, "overlays", text="", icon="OVERLAY")
