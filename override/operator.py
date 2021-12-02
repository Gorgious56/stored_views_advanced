import bpy
from stored_views_advanced.preferences.helper import get_preferences


class SVA_OT__stored_views_store(bpy.types.Operator):
    bl_idname = "stored_views.save"
    bl_label = "Save Current"
    bl_description = "Save the view 3d current state"

    index: bpy.props.IntProperty()

    def execute(self, context):
        from space_view3d_stored_views.operators import VIEW3D_stored_views_save

        VIEW3D_stored_views_save.execute(self, context)

        if self.index < 0:
            context.scene.sva.add()
            correct_index = len(context.scene.sva) - 1
        else:
            correct_index = self.index

        prefs = get_preferences(context).settings
        if prefs.sync_outliner:
            bpy.ops.sva.outliner_store_or_restore_settings(store=True, index=correct_index)
        if prefs.sync_objects:
            bpy.ops.sva.objects_store_or_restore_settings(store=True, index=correct_index)
        if prefs.sync_collections:
            bpy.ops.sva.collections_store_or_restore_settings(store=True, index=correct_index)
        if prefs.sync_view_layers:
            bpy.ops.sva.view_layer_store_or_restore_settings(store=True, index=correct_index)
        return {"FINISHED"}


class SVA_OT_stored_views_restore(bpy.types.Operator):
    bl_idname = "stored_views.set"
    bl_label = "Set"
    bl_description = "Update the view 3D according to this view"

    index: bpy.props.IntProperty()

    def execute(self, context):
        from space_view3d_stored_views.operators import VIEW3D_stored_views_set

        VIEW3D_stored_views_set.execute(self, context)

        prefs = get_preferences(context).settings
        if prefs.sync_outliner:
            bpy.ops.sva.outliner_store_or_restore_settings(store=False, index=self.index)
        if prefs.sync_objects:
            bpy.ops.sva.objects_store_or_restore_settings(store=False, index=self.index)
        if prefs.sync_collections:
            bpy.ops.sva.collections_store_or_restore_settings(store=False, index=self.index)
        if prefs.sync_view_layers:
            bpy.ops.sva.view_layer_store_or_restore_settings(store=False, index=self.index)
        return {"FINISHED"}


class SVA_stored_views_delete(bpy.types.Operator):
    bl_idname = "stored_views.delete"
    bl_label = "Delete"
    bl_description = "Delete this view"

    index: bpy.props.IntProperty()

    def execute(self, context):
        from space_view3d_stored_views.operators import VIEW3D_stored_views_delete

        VIEW3D_stored_views_delete.execute(self, context)

        context.scene.sva.remove(self.index)

        return {"FINISHED"}
