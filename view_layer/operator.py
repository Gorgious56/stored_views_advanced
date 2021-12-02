import bpy
from stored_views_advanced.outliner.helper import get_outliner_area
from stored_views_advanced.view_layer.helper import get_family_down


class SVA_OT_view_layer_store_or_restore_settings(bpy.types.Operator):
    bl_label = "Store / Restore view Layer Settings"
    bl_idname = "sva.view_layer_store_or_restore_settings"

    index:  bpy.props.IntProperty()
    store: bpy.props.BoolProperty()

    def execute(self, context):
        view_layers_props = context.scene.sva[self.index].view_layers

        view_layers_mapping = {vl.name: vl for vl in view_layers_props}
        for view_layer in context.scene.view_layers:
            view_layer_props = view_layers_mapping.get(view_layer.name)
            if view_layer_props is None:
                view_layer_props = view_layers_props.add()
                view_layer_props.name = view_layer.name

            layer_collections = get_family_down(view_layer.layer_collection)
            layer_collections_mapping = {l_c.name: l_c for l_c in view_layer_props.layer_collections_props}
            for layer_collection in layer_collections:
                layer_collection_props = layer_collections_mapping.get(layer_collection.collection.name)
                if layer_collection_props is None:
                    layer_collection_props = view_layer_props.layer_collections_props.add()
                    layer_collection_props.name = layer_collection.collection.name
                if self.store:
                    layer_collection_props.store(layer_collection)
                else:
                    layer_collection_props.restore(layer_collection)
        
        get_outliner_area(context).tag_redraw()

        return {"FINISHED"}
