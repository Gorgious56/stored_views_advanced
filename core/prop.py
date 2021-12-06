import bpy
from stored_views_advanced.outliner.prop import Properties as OutlinerProperties
from stored_views_advanced.object.prop import Properties as ObjectProperties
from stored_views_advanced.view_layer.prop import Properties as ViewLayerProperties
from stored_views_advanced.collection.prop import Properties as CollectionProperties
from stored_views_advanced.viewport.prop import ViewProperties as ViewportProperties
from enum import Enum


class StoreType(Enum):
    GLOBAL = "global"
    VIEW_LAYER = "view_layer"


class ViewSyncSettings(bpy.types.PropertyGroup):
    outliner: bpy.props.BoolProperty(default=True, name="Sync Outliner")
    objects: bpy.props.BoolProperty(default=True, name="Sync Objects")
    view_layers: bpy.props.BoolProperty(default=True, name="Sync View Layers")
    collections: bpy.props.BoolProperty(default=True, name="Sync Collections")
    viewport: bpy.props.BoolProperty(default=True, name="Sync Viewport")
    shading: bpy.props.BoolProperty(default=True, name="Sync Shading")
    overlays: bpy.props.BoolProperty(default=True, name="Sync Overlays")


class ViewStoreStatus(bpy.types.PropertyGroup):
    outliner: bpy.props.BoolProperty()
    objects: bpy.props.BoolProperty()
    view_layers: bpy.props.BoolProperty()
    collections: bpy.props.BoolProperty()
    viewport: bpy.props.BoolProperty()
    shading: bpy.props.BoolProperty()
    overlays: bpy.props.BoolProperty()


class ViewSettingsStore(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty()
    sync_settings: bpy.props.PointerProperty(type=ViewSyncSettings)
    stored_props: bpy.props.PointerProperty(type=ViewStoreStatus)
    outliner: bpy.props.PointerProperty(type=OutlinerProperties)
    objects: bpy.props.CollectionProperty(type=ObjectProperties)
    view_layers: bpy.props.CollectionProperty(type=ViewLayerProperties)
    collections: bpy.props.CollectionProperty(type=CollectionProperties)
    viewport: bpy.props.PointerProperty(type=ViewportProperties)

    SETTINGS_TYPES = ("outliner", "objects", "collections", "view_layers", "viewport", "shading", "overlays")

    def get_or_create_object_props(self, obj):
        for obj_props in self.objects:
            if obj_props.obj == obj:
                return obj_props
        new = self.objects.add()
        new.obj = obj
        return new


class StorePointer(bpy.types.PropertyGroup):
    store: bpy.props.CollectionProperty(type=ViewSettingsStore)
    index: bpy.props.IntProperty()
    name: bpy.props.StringProperty()

    def __len__(self):
        return len(self.store)

    def get(self, index, default=None):
        if isinstance(index, int):
            return self.store[index] or default
        elif isinstance(index, str):
            return next(e for e in self.store if e.name == index)

    @property
    def active(self):
        return self.get(self.index)

    def add(self, name=""):
        new = self.store.add()
        new.name = name
        return new

    def remove(self, index):
        if index < 0:
            return
        self.store.remove(index)
        if index == self.index:
            self.index = max(0, index - 1)


class StoredViewsAdvanced(bpy.types.PropertyGroup):
    store_global: bpy.props.PointerProperty(type=StorePointer)
    store_view_layer: bpy.props.PointerProperty(type=StorePointer)

    def get_store(self, store_type):
        return {
            StoreType.GLOBAL.value: self.store_global,
            StoreType.VIEW_LAYER.value: self.store_view_layer,
        }[store_type]


def register():
    bpy.types.Scene.sva = bpy.props.PointerProperty(type=StoredViewsAdvanced)

def unregister():
    del bpy.types.Scene.sva
