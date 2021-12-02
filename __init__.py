from . import auto_load
import bpy

bl_info = {
    "name": "Stored Views Advanced",
    "blender": (2, 93, 0),
    "category": "3D View",
    "version": (0, 0, 1),
    "author": "Gorgious56",
    "description": "Save and restore User defined views, pov, layers and display config",
}


def register():
    auto_load.init()
    auto_load.register()


def unregister():
    auto_load.unregister()
    from space_view3d_stored_views.operators import VIEW3D_stored_views_save
    bpy.utils.register_class(VIEW3D_stored_views_save)
    from space_view3d_stored_views.operators import VIEW3D_stored_views_set
    bpy.utils.register_class(VIEW3D_stored_views_set)
    from space_view3d_stored_views.operators import VIEW3D_stored_views_delete
    bpy.utils.register_class(VIEW3D_stored_views_delete)
