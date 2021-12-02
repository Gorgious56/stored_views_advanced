import bpy


class SVA_PT_viewport(bpy.types.Panel):    
    bl_label = "Stored Views Advanced"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "View"
    bl_options = {'DEFAULT_CLOSED'}


    def draw(self, context):
        layout = self.layout

        layout.operator("sva.outliner_store_or_restore_settings", text="Store Outliner Settings").store = True
        layout.operator("sva.outliner_store_or_restore_settings", text="Restore Outliner Settings").store = False
        layout.operator("sva.objects_store_or_restore_settings", text="Store Objects Settings").store = True
        layout.operator("sva.objects_store_or_restore_settings", text="Restore Objects Settings").store = False
        layout.operator("sva.view_layer_store_or_restore_settings", text="Store View Layer Settings").store = True
        layout.operator("sva.view_layer_store_or_restore_settings", text="Restore View Layer Settings").store = False
        layout.operator("sva.collections_store_or_restore_settings", text="Store Collections Settings").store = True
        layout.operator("sva.collections_store_or_restore_settings", text="Restore Collections Settings").store = False
