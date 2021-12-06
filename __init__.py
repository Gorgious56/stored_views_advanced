from . import auto_load

bl_info = {
    "name": "Stored Views Advanced",
    "blender": (2, 93, 0),
    "category": "3D View",
    "version": (1, 0, 0),
    "author": "Gorgious56",
    "description": "Save and restore User defined views, pov, layers and display config",
}


def register():
    auto_load.init()
    auto_load.register()


def unregister():
    auto_load.unregister()
