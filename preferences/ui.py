import bpy

from .prop import DefaultSettings


class SVAAddonPreferences(bpy.types.AddonPreferences):
    bl_idname = "stored_views_advanced"

    settings: bpy.props.PointerProperty(type=DefaultSettings)

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        box.label(text="Default Synchronization Settings")
        for attr in self.settings.__annotations__:
            box.prop(self.settings, attr)
