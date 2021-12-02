import bpy
from stored_views_advanced.outliner.helper import get_outliner_area


class SVA_OT_objects_store_or_restore_settings(bpy.types.Operator):
    bl_label = "Store / Restore Objects Settings"
    bl_idname = "sva.objects_store_or_restore_settings"

    index:  bpy.props.IntProperty()
    store: bpy.props.BoolProperty()

    def execute(self, context):
        scene = context.scene
        sva_props = scene.sva[self.index]
        for obj in scene.objects:
            props = sva_props.get_or_create_object_props(obj)

            if self.store:
                props.store(obj, scene)
            else:
                props.restore(obj, scene)
                get_outliner_area(context).tag_redraw()


        return {"FINISHED"}
