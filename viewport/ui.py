import bpy
from stored_views_advanced.core.ui import draw_store_list


class SVA_PT_viewport(bpy.types.Panel):
    bl_label = "Stored Views Advanced"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "View"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        draw_store_list(self.layout, context, "global")
