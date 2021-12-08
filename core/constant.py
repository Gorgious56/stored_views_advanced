import bpy


ICONS = {
    "scene": "SCENE_DATA",
    "world": "WORLD",
    "collections": "OUTLINER_COLLECTION",
    "objects": "OBJECT_DATAMODE",
    "view_layers": "RENDERLAYERS",
    "outliner": "OUTLINER",
    "viewport": "VIEW3D",
    "shading": "SHADING_RENDERED",
    "overlays": "OVERLAY",
}


SETTINGS_TYPES = ICONS.keys()


TYPE_MAPPING = {
    "scene": bpy.types.Scene,
    "world": bpy.types.World,
    "collections": bpy.types.Collection,
    "objects": bpy.types.Object,
    "view_layers": str,
}


TYPE_STORING = TYPE_MAPPING.keys()
