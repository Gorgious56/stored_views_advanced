import bpy

from .prop import Settings


class SVAAddonPreferences(bpy.types.AddonPreferences):
    bl_idname = "stored_views_advanced"

    settings: bpy.props.PointerProperty(type=Settings)

    def draw(self, context):
        layout = self.layout
        layout.prop(self.settings, "sync_objects")
        layout.prop(self.settings, "sync_collections")
        layout.prop(self.settings, "sync_view_layers")
        layout.prop(self.settings, "sync_outliner")
