import bpy
from stored_views_advanced.outliner.helper import get_outliner_area
from stored_views_advanced.view_layer.helper import get_family_down


class SVA_OT_collections_store_or_restore_settings(bpy.types.Operator):
    bl_label = "Store / Restore Collections Settings"
    bl_idname = "sva.collections_store_or_restore_settings"

    index:  bpy.props.IntProperty()
    store: bpy.props.BoolProperty()

    def execute(self, context):
        outliner_area = get_outliner_area(context)

        collections_props = context.scene.sva[self.index].collections
        collections_props_mapping = {c.name: c for c in collections_props}

        for col in get_family_down(context.scene.collection):
            col_props = collections_props_mapping.get(col.name)
            if col_props is None:
                col_props = collections_props.add()
                col_props.name = col.name
            if self.store:
                col_props.store(col)
            else:
                col_props.restore(col)

        outliner_area.tag_redraw()

        return {"FINISHED"}
