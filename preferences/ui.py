import bpy

from stored_views_advanced.core.prop import ViewSyncSettings
from stored_views_advanced.core.constant import ICONS
from .prop import AdvancedSettings, EnableSettings


class SVAAddonPreferences(bpy.types.AddonPreferences):
    bl_idname = "stored_views_advanced"

    panel: bpy.props.EnumProperty(
        items=(
            ("0", "Defaults", ""),
            ("1", "Advanced", "")
        )
    )
    defaults: bpy.props.PointerProperty(type=ViewSyncSettings)
    advanced: bpy.props.PointerProperty(type=AdvancedSettings)
    enabled: bpy.props.PointerProperty(type=EnableSettings)

    def draw(self, context):
        layout = self.layout
        layout.row().prop_tabs_enum(self, "panel")
        if self.panel == "0":
            box = layout.box()
            box.label(text="Settings to synchronize by default when storing a new view")
            for attr in self.defaults.__annotations__:
                row = box.row()
                row.label(text="", icon=ICONS.get(attr, "BLANK1"))
                row.prop(self.defaults, attr)
        elif self.panel == "1":
            box = layout.box()
            box.label(text="Data types which can hold stored views and if they use regular or advanced mode")
            for setting in self.advanced.__annotations__:
                row = box.row(align=True)
                row.label(text=setting.title().replace("_", " "), icon=ICONS.get(setting, "BLANK1"))
                row.prop(self.enabled, setting, text="Enable", toggle=True)
                advanced = row.row(align=True)
                advanced.prop(self.advanced, setting, text="Advanced Mode", toggle=True)
                advanced.enabled = getattr(self.enabled, setting)
