import bpy
from bpy.types import Operator
from bpy.props import StringProperty, IntProperty, BoolProperty
from stored_views_advanced.viewport.helper import get_viewport_area
from stored_views_advanced.outliner.helper import get_outliner_area


def store_op_execute(self, context):
    copy_item = entries[self.data_name](context)
    entry = context.scene.sva.get(self.store).get(self.index)
    data = getattr(entry, self.data_name)
    if self.is_storing:
        data.store(copy_item)
    else:
        data.restore(copy_item)
        get_outliner_area(context).tag_redraw()
    return {"FINISHED"}


entries = {
    "world": lambda context: context.scene.world,
    "scene": lambda context: context.scene,
    "viewport": lambda context: get_viewport_area(context).spaces[0],
    "shading": lambda context: get_viewport_area(context).spaces[0].shading,
    "overlays": lambda context: get_viewport_area(context).spaces[0].overlay,
    "outliner": lambda context: get_outliner_area(context).spaces[0],
}

store_ops = [
    type(
        f"SVA_OT_{name}_store_settings",
        (Operator,),
        {
            "bl_idname": f"sva.{name}_store_settings",
            "bl_label": f"Store {name.upper()} Settings",
            "execute": store_op_execute,
            "__annotations__": {
                "store": StringProperty(),
                "index": IntProperty(),
                "data_name": StringProperty(default=name),
                "is_storing": BoolProperty(),
            },
        },
    )
    for name in entries.keys()
]


def register():
    for op in store_ops:
        bpy.utils.register_class(op)


def unregister():
    for op in store_ops:
        bpy.utils.unregister_class(op)
