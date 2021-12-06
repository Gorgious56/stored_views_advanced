import bpy
from bpy.props import StringProperty, IntProperty
from .helper import get_viewport_area


class SVA_OT_viewport_store_settings(bpy.types.Operator):
    bl_label = "Store Viewport Settings"
    bl_idname = "sva.viewport_store_settings"

    container: StringProperty()
    index: IntProperty()

    def execute(self, context):
        viewport_space = get_viewport_area(context).spaces[0]
        entry = context.scene.sva.get_store(self.container).get(self.index)
        entry.viewport.store(viewport_space)
        entry.viewport.region_3d.store(viewport_space.region_3d)
        return {"FINISHED"}


class SVA_OT_viewport_restore_settings(bpy.types.Operator):
    bl_label = "Restore Viewport Settings"
    bl_idname = "sva.viewport_restore_settings"

    container: StringProperty()
    index: IntProperty()

    def execute(self, context):
        viewport_space = get_viewport_area(context).spaces[0]
        entry = context.scene.sva.get_store(self.container).get(self.index)
        entry.viewport.restore(viewport_space)
        entry.viewport.region_3d.restore(viewport_space.region_3d)
        return {"FINISHED"}


class SVA_OT_shading_store_settings(bpy.types.Operator):
    bl_label = "Store Shading Settings"
    bl_idname = "sva.shading_store_settings"

    container: StringProperty()
    index: IntProperty()

    def execute(self, context):
        viewport_space = get_viewport_area(context).spaces[0]
        entry = context.scene.sva.get_store(self.container).get(self.index)
        entry.viewport.shading.store(viewport_space.shading)
        return {"FINISHED"}


class SVA_OT_shading_restore_settings(bpy.types.Operator):
    bl_label = "Restore Shading Settings"
    bl_idname = "sva.shading_restore_settings"

    container: StringProperty()
    index: IntProperty()

    def execute(self, context):
        viewport_space = get_viewport_area(context).spaces[0]
        entry = context.scene.sva.get_store(self.container).get(self.index)
        entry.viewport.shading.restore(viewport_space.shading)
        return {"FINISHED"}


class SVA_OT_overlays_store_settings(bpy.types.Operator):
    bl_label = "Store Overlays Settings"
    bl_idname = "sva.overlays_store_settings"

    container: StringProperty()
    index: IntProperty()

    def execute(self, context):
        viewport_space = get_viewport_area(context).spaces[0]
        entry = context.scene.sva.get_store(self.container).get(self.index)
        entry.viewport.overlay.store(viewport_space.overlay)
        return {"FINISHED"}


class SVA_OT_overlays_restore_settings(bpy.types.Operator):
    bl_label = "Restore Overlays Settings"
    bl_idname = "sva.overlays_restore_settings"

    container: StringProperty()
    index: IntProperty()

    def execute(self, context):
        viewport_space = get_viewport_area(context).spaces[0]
        entry = context.scene.sva.get_store(self.container).get(self.index)
        entry.viewport.overlay.restore(viewport_space.overlay)
        return {"FINISHED"}
