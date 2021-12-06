import bpy
from stored_views_advanced.preferences.helper import get_preferences


class SVA_OT_add_entry(bpy.types.Operator):
    bl_label = "Add Entry"
    bl_idname = "sva.add_entry"

    container: bpy.props.StringProperty(default="global")
    name: bpy.props.StringProperty()

    def execute(self, context):
        sva_props = getattr(context.scene.sva, f"store_{self.container}")
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
            print(attr)
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
