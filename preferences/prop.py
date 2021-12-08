import bpy
from bpy.props import BoolProperty, PointerProperty, StringProperty, CollectionProperty, IntProperty
from stored_views_advanced.core.constant import TYPE_MAPPING, TYPE_STORING


AdvancedSettings = type(
    "AdvancedSettings",
    (bpy.types.PropertyGroup,),
    {
        "__annotations__": {
            data: BoolProperty(default=False if data != "collections" else True, name=data.title().replace("_", " "))
            for data in TYPE_STORING
        }
    },
)


EnableSettings = type(
    "EnableSettings",
    (bpy.types.PropertyGroup,),
    {
        "__annotations__": {
            data: BoolProperty(default=True, name=data.title().replace("_", " ")) for data in TYPE_STORING
        }
    },
)
