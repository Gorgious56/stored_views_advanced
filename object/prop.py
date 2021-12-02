import bpy
from stored_views_advanced.shared.prop import PropsStore


class Properties(bpy.types.PropertyGroup, PropsStore):
    obj: bpy.props.PointerProperty(type=bpy.types.Object)
    hide_select: bpy.props.BoolProperty()
    hide_eye_icon: bpy.props.BoolProperty()
    hide_viewport: bpy.props.BoolProperty()
    hide_render: bpy.props.BoolProperty()

    def store(self, copy_from, scene):
        super().store(copy_from)
        self.hide_eye_icon = copy_from.hide_get()

    def restore(self, copy_to, scene):
        super().restore(copy_to)
        copy_to.hide_set(self.hide_eye_icon)
