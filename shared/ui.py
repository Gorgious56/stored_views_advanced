import bpy
from bpy.types import Panel
from stored_views_advanced.core.ui import draw_id, draw_store_list
from stored_views_advanced.preferences.helper import get_preferences


def draw(self, context, name):
    prefs = get_preferences(context).advanced
    if getattr(prefs, name):
        draw_store_list(self.layout, context, name)
    else:
        draw_id(self.layout, context, name)


entries = {
    "collections": lambda self, context: draw(self, context, "collections"),
    "scene": lambda self, context: draw(self, context, "scene"),
    "world": lambda self, context: draw(self, context, "world"),
}

entries_name = {
    "collections": "collection",
}
panels = [
    type(
        f"SVA_PT_{name}_stored_view",
        (Panel,),
        {
            "bl_idname": f"SVA_PT_{name}_stored_view",
            "bl_label": f"Stored Views",
            "bl_space_type": "PROPERTIES",
            "bl_region_type": "WINDOW",
            "bl_context": entries_name.get(name, name),
            "draw": entries[name],
        },
    )
    for name in entries.keys()
]

def register():
    for op in panels:
        bpy.utils.register_class(op)


def unregister():
    for op in panels:
        bpy.utils.unregister_class(op)
