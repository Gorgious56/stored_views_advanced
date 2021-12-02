import bpy
from stored_views_advanced.shared.prop import PropsStore


class Properties(bpy.types.PropertyGroup, PropsStore):
    hide_viewport: bpy.props.BoolProperty()
    hide_render: bpy.props.BoolProperty()
    hide_select: bpy.props.BoolProperty()
