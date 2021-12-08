from bpy.types import PropertyGroup
from bpy.props import (
    FloatProperty,
    CollectionProperty,
    FloatVectorProperty,
    StringProperty,
    EnumProperty,
    BoolProperty,
    BoolVectorProperty,
    IntProperty,
    PointerProperty,
)
from stored_views_advanced.shared.prop import PropsStore, StringPropertyGroup


class WorldLightingProperties(PropertyGroup, PropsStore):
    ao_factor: FloatProperty()
    distance: FloatProperty()
    use_ambient_occlusion: BoolProperty()


class WorldMistProperties(PropertyGroup, PropsStore):
    depth: FloatProperty()
    falloff: StringProperty()
    height: FloatProperty()
    intensity: FloatProperty()
    start: FloatProperty()
    use_mist: BoolProperty()


class CyclesProperties(PropertyGroup, PropsStore):
    sampling_method: StringProperty()
    sample_map_resolution: IntProperty()
    max_bounces: IntProperty()
    volume_sampling: StringProperty()
    volume_interpolation: StringProperty()
    homogeneous_volume: BoolProperty()
    volume_step_size: FloatProperty()


class CyclesVisibilityProperties(PropertyGroup, PropsStore):
    camera: BoolProperty()
    diffuse: BoolProperty()
    glossy: BoolProperty()
    transmission: BoolProperty()
    scatter: BoolProperty()


class Properties(PropertyGroup, PropsStore):
    color: FloatVectorProperty()
    use_nodes: BoolProperty()
    sub_props_store: CollectionProperty(type=StringPropertyGroup)
    cycles: PointerProperty(type=CyclesProperties)
    cycles_visibility: PointerProperty(type=CyclesVisibilityProperties)
    light_settings: PointerProperty(type=WorldLightingProperties)
    mist_settings: PointerProperty(type=WorldMistProperties)
    # node_tree : Not supported
