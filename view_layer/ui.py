import bpy
from stored_views_advanced.core.ui import draw_store_list


class GU_PT_view_layer_stored_view(bpy.types.Panel):
    bl_label = "Stored Views"
    bl_idname = "GU_PT_view_layer_stored_view"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "view_layer"

    def draw(self, context):
        draw_store_list(self.layout, context, "view_layer")
