import bpy
from stored_views_advanced.outliner.helper import get_outliner_area


class SVA_OT_test(bpy.types.Operator):
    bl_label = "Store / Restore Outliner Settings"
    bl_idname = "sva.outliner_store_or_restore_settings"

    index:  bpy.props.IntProperty()
    store: bpy.props.BoolProperty()

    def execute(self, context):
        outliner_area = get_outliner_area(context)
        space = outliner_area.spaces[0]

        outliner_props = context.scene.sva[self.index].outliner

        if self.store:
            outliner_props.store(space)
        else:
            outliner_props.restore(space)
            get_outliner_area(context).tag_redraw()

        return {"FINISHED"}
