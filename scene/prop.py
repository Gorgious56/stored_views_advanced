import bpy
from stored_views_advanced.outliner.prop import Properties as OutlinerProperties
from stored_views_advanced.object.prop import Properties as ObjectProperties
from stored_views_advanced.view_layer.prop import Properties as ViewLayerProperties
from stored_views_advanced.collection.prop import Properties as CollectionProperties


class StoredViewsAdvanced(bpy.types.PropertyGroup):
    outliner: bpy.props.PointerProperty(type=OutlinerProperties)
    objects: bpy.props.CollectionProperty(type=ObjectProperties)
    view_layers: bpy.props.CollectionProperty(type=ViewLayerProperties)
    collections: bpy.props.CollectionProperty(type=CollectionProperties)

    def get_or_create_object_props(self, obj):
        for obj_props in self.objects:
            if obj_props.obj == obj:
                return obj_props
        new = self.objects.add()
        new.obj = obj
        return new

def register():
    bpy.types.Scene.sva = bpy.props.CollectionProperty(type=StoredViewsAdvanced)
