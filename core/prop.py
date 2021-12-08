import bpy
from stored_views_advanced.outliner.prop import Properties as OutlinerProperties
from stored_views_advanced.object.prop import Properties as ObjectProperties
from stored_views_advanced.view_layer.prop import Properties as ViewLayerProperties
from stored_views_advanced.collection.prop import Properties as CollectionProperties
from stored_views_advanced.viewport.prop import ViewProperties, OverlayProperties, ShadingProperties


class ViewSyncSettings(bpy.types.PropertyGroup):
    outliner: bpy.props.BoolProperty(default=True, name="Synchronize Outliner")
    objects: bpy.props.BoolProperty(default=True, name="Synchronize Objects")
    view_layers: bpy.props.BoolProperty(default=True, name="Synchronize View Layers")
    collections: bpy.props.BoolProperty(default=True, name="Synchronize Collections")
    viewport: bpy.props.BoolProperty(default=True, name="Synchronize Viewport")
    shading: bpy.props.BoolProperty(default=True, name="Synchronize Shading")
    overlays: bpy.props.BoolProperty(default=True, name="Synchronize Overlays")


class ViewStoreStatus(bpy.types.PropertyGroup):
    outliner: bpy.props.BoolProperty()
    objects: bpy.props.BoolProperty()
    view_layers: bpy.props.BoolProperty()
    collections: bpy.props.BoolProperty()
    viewport: bpy.props.BoolProperty()
    shading: bpy.props.BoolProperty()
    overlays: bpy.props.BoolProperty()


    viewport: PointerProperty(type=ViewProperties)
    shading: PointerProperty(type=ShadingProperties)
    overlays: PointerProperty(type=OverlayProperties)

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

    def get_index(self, entry):
        for i, e in enumerate(self.store):
            if e == entry:
                return i
        return -1

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
    store_scene: bpy.props.PointerProperty(type=StorePointer)

    def get_store(self, store_name):
        return getattr(self, f"store_{store_name}")


def register():
    bpy.types.Scene.sva = bpy.props.PointerProperty(type=StoredViewsAdvanced)


def unregister():
    del bpy.types.Scene.sva
