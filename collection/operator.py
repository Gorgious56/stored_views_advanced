
import bpy
from stored_views_advanced.outliner.helper import get_outliner_area
from stored_views_advanced.view_layer.helper import get_family_down


def iterate_collections(context, container, index, parent, do):
    collections_props = context.scene.sva.get_store(container).get(index).collections
    collections_props_mapping = {c.name: c for c in collections_props}
    for col in get_family_down(parent):
        col_props = collections_props_mapping.get(col.name)
        if col_props is None:
            col_props = collections_props.add()
            col_props.name = col.name
        do(col_props, col)


class SVA_OT_collections_store_settings(bpy.types.Operator):
    bl_label = "Store Collections Settings"
    bl_idname = "sva.collections_store_settings"

    container: bpy.props.StringProperty()
    index: bpy.props.IntProperty()

    def execute(self, context):
        iterate_collections(
            context, self.container, self.index, context.scene.collection, lambda props, col: props.store(col)
        )
        return {"FINISHED"}

class SVA_OT_collections_restore_settings(bpy.types.Operator):
    bl_label = "Restore Collections Settings"
    bl_idname = "sva.collections_restore_settings"

    container: bpy.props.StringProperty()
    index: bpy.props.IntProperty()

    def execute(self, context):
        iterate_collections(
            context, self.container, self.index, context.scene.collection, lambda props, col: props.restore(col)
        )
        get_outliner_area(context).tag_redraw()
        return {"FINISHED"}
