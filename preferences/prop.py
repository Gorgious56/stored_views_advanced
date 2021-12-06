import bpy


class DefaultSettings(bpy.types.PropertyGroup):
    sync_objects: bpy.props.BoolProperty(default=True, name="Synchronize Objects")
    sync_collections: bpy.props.BoolProperty(default=True, name="Synchronize Collections")
    sync_view_layers: bpy.props.BoolProperty(default=True, name="Synchronize View Layers")
    sync_outliner: bpy.props.BoolProperty(default=True, name="Synchronize Outliner Filters and Toggles")
    sync_viewport: bpy.props.BoolProperty(default=True, name="Synchronize Viewport")
    sync_shading: bpy.props.BoolProperty(default=True, name="Synchronize Shading")
    sync_overlays: bpy.props.BoolProperty(default=True, name="Synchronize Overlays")
