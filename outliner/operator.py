import bpy
from stored_views_advanced.outliner.helper import get_outliner_area


class SVA_OT_outliner_store_settings(bpy.types.Operator):
    bl_label = "Store Outliner Settings"
    bl_idname = "sva.outliner_store_settings"

    container: bpy.props.StringProperty()
    index:  bpy.props.IntProperty()

    def execute(self, context):
        outliner_area = get_outliner_area(context)
        space = outliner_area.spaces[0]

        outliner_props = context.scene.sva.get_store(self.container).get(self.index).outliner
        outliner_props.store(space)

        return {"FINISHED"}

class SVA_OT_outliner_restore_settings(bpy.types.Operator):
    bl_label = "Restore Outliner Settings"
    bl_idname = "sva.outliner_restore_settings"

    container: bpy.props.StringProperty()
    index:  bpy.props.IntProperty()

    def execute(self, context):
        outliner_area = get_outliner_area(context)
        space = outliner_area.spaces[0]

        outliner_props = context.scene.sva.get_store(self.container).get(self.index).outliner
        outliner_props.restore(space)
        get_outliner_area(context).tag_redraw()

        return {"FINISHED"}