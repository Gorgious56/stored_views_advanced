import bpy
from stored_views_advanced.shared.prop import PropsStore


class LayerCollectionProps(bpy.types.PropertyGroup, PropsStore):
    exclude: bpy.props.BoolProperty()
    hide_viewport: bpy.props.BoolProperty()
    holdout: bpy.props.BoolProperty()
    indirect_only: bpy.props.BoolProperty()


class Properties(bpy.types.PropertyGroup):
    layer_collections_props: bpy.props.CollectionProperty(type=LayerCollectionProps)
