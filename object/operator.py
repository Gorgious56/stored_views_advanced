import bpy
from stored_views_advanced.outliner.helper import get_outliner_area


class SVA_OT_objects_store_settings(bpy.types.Operator):
    bl_label = "Store Objects Settings"
    bl_idname = "sva.objects_store_settings"

    store: bpy.props.StringProperty()
    index: bpy.props.IntProperty()

    def execute(self, context):
        scene = context.scene
        sva_props = scene.sva.get(self.store).get(self.index)
        for obj in scene.objects:
            sva_props.get_or_create_object_props(obj).store(obj, scene)

        return {"FINISHED"}


class SVA_OT_objects_restore_settings(bpy.types.Operator):
    bl_label = "Restore Objects Settings"
    bl_idname = "sva.objects_restore_settings"

    store: bpy.props.StringProperty()
    index: bpy.props.IntProperty()

    def execute(self, context):
        scene = context.scene
        sva_props = scene.sva.get(self.store).get(self.index)
        for obj in scene.objects:
            sva_props.get_or_create_object_props(obj).restore(obj, scene)

        get_outliner_area(context).tag_redraw()

        return {"FINISHED"}
