import bpy
from bpy.types import PropertyGroup, Scene, World, Collection, Object, ID
from bpy.props import BoolProperty, PointerProperty, StringProperty, CollectionProperty, IntProperty
from stored_views_advanced.outliner.prop import Properties as OutlinerProperties
from stored_views_advanced.object.prop import Properties as ObjectProperties
from stored_views_advanced.view_layer.prop import Properties as ViewLayerProperties
from stored_views_advanced.collection.prop import Properties as CollectionProperties
from stored_views_advanced.viewport.prop import ViewProperties, OverlayProperties, ShadingProperties
from stored_views_advanced.world.prop import Properties as WorldProperties
from stored_views_advanced.scene.prop import Properties as SceneProperties
from .constant import SETTINGS_TYPES, TYPE_MAPPING


ViewSyncSettings = type(
    "ViewSyncSettings",
    (PropertyGroup,),
    {
        "__annotations__": {
            data: BoolProperty(default=True, name=data.title().replace("_", " ")) for data in SETTINGS_TYPES
        }
    },
)


ViewStoreStatus = type(
    "ViewStoreStatus",
    (PropertyGroup,),
    {"__annotations__": {data: BoolProperty() for data in SETTINGS_TYPES}},
)


class StoreID(PropertyGroup):
    scene: PointerProperty(type=Scene)
    collection: PointerProperty(type=Collection)
    view_layer: StringProperty()  # Can not store by ID
    object: PointerProperty(type=Object)
    world: PointerProperty(type=World)
    name: StringProperty()

    def get(self):
        return getattr(self, self.name) if self.name else None

    MAPPING = {
        Scene: "scene",
        Collection: "collection",
    }

    def set(self, value):
        for name, _type in TYPE_MAPPING.items():
            if isinstance(value, _type):
                self.name = name
                if isinstance(_type, str):
                    value = value.name
        setattr(self, self.name, value)


class ViewSettingsStore(PropertyGroup):
    name: StringProperty()

    sync_settings: PointerProperty(type=ViewSyncSettings)

    stored_props: PointerProperty(type=ViewStoreStatus)

    scene: PointerProperty(type=SceneProperties)
    outliner: PointerProperty(type=OutlinerProperties)
    objects: CollectionProperty(type=ObjectProperties)
    view_layers: CollectionProperty(type=ViewLayerProperties)
    collections: CollectionProperty(type=CollectionProperties)
    viewport: PointerProperty(type=ViewProperties)
    shading: PointerProperty(type=ShadingProperties)
    overlays: PointerProperty(type=OverlayProperties)
    world: PointerProperty(type=WorldProperties)

    identifier: PointerProperty(type=StoreID)

    def get_or_create_object_props(self, obj):
        for obj_props in self.objects:
            if obj_props.obj == obj:
                return obj_props
        new = self.objects.add()
        new.obj = obj
        return new


class StorePointer(PropertyGroup):
    settings: CollectionProperty(type=ViewSettingsStore)
    index: IntProperty()
    name: StringProperty()

    def __len__(self):
        return len(self.settings)

    def get(self, index, default=None):
        """If index is (int), returns entry at index
        If index is (str), returns entry which name is index
        If index is (ID), returns entry which identifier is index"""
        if isinstance(index, int):
            try:
                return self.settings[index] or default
            except IndexError:
                return None
        elif isinstance(index, str):
            return next(e for e in self.settings if e.name == index)
        elif isinstance(index, ID):
            try:
                return next(e for e in self.settings if e.identifier.get() == index)
            except StopIteration:
                return None

    def get_index(self, entry):
        for i, e in enumerate(self.settings):
            if e == entry:
                return i
        return -1

    @property
    def active(self):
        return self.get(self.index)

    def add(self, name=""):
        new = self.settings.add()
        new.name = name
        return new

    def remove(self, index):
        if index < 0:
            return
        self.settings.remove(index)
        if index == self.index:
            self.index = max(0, index - 1)


class StoredViewsAdvanced(PropertyGroup):
    stores: CollectionProperty(type=StorePointer)

    inspect: BoolProperty()

    def get(self, store_name):
        return next(s for s in self.stores if s.name == store_name)


def register():
    Scene.sva = PointerProperty(type=StoredViewsAdvanced)


def unregister():
    del Scene.sva
