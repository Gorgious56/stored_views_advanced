from bpy.types import (
    PropertyGroup,
    Object,
    Scene,
    MovieClip,
    Collection,
    GreasePencil,
    NodeTree,
    World,
)
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
from stored_views_advanced.shared.prop import PropsStore


class Properties(PropertyGroup, PropsStore):
    active_clip: PointerProperty(type=MovieClip)
    # animation_data: TODO
    audio_distance_model: StringProperty()
    audio_doppler_factor: FloatProperty()
    audio_doppler_speed: FloatProperty()
    audio_volume: FloatProperty()
    background_set: PointerProperty(type=Scene)
    camera: PointerProperty(type=Object)
    collection: PointerProperty(type=Collection)
    # cursor: TODO https://docs.blender.org/api/current/bpy.types.View3DCursor.html#bpy.types.View3DCursor
    # cycles : TODO
    # cycles_curves: TODO
    # display: TODO https://docs.blender.org/api/current/bpy.types.SceneDisplay.html#bpy.types.SceneDisplay
    # display_settings: TODO https://docs.blender.org/api/current/bpy.types.ColorManagedDisplaySettings.html#bpy.types.ColorManagedDisplaySettings
    # eevee: TODO https://docs.blender.org/api/current/bpy.types.SceneEEVEE.html#bpy.types.SceneEEVEE
    frame_current: IntProperty()
    frame_current_final: IntProperty()
    frame_end: IntProperty()
    frame_float: FloatProperty()
    frame_preview_end: IntProperty()
    frame_preview_start: IntProperty()
    frame_start: IntProperty()
    frame_step: IntProperty()
    frame_subframe: FloatProperty()
    gravity: FloatVectorProperty()
    grease_pencil: PointerProperty(type=GreasePencil)
    # grease_pencil_settings: TODO https://docs.blender.org/api/current/bpy.types.SceneGpencil.html#bpy.types.SceneGpencil
    is_nla_tweakmode: BoolProperty()
    # keying_sets: TODO https://docs.blender.org/api/current/bpy.types.KeyingSets.html#bpy.types.KeyingSets
    # keying_sets_all: TODO https://docs.blender.org/api/current/bpy.types.KeyingSetsAll.html#bpy.types.KeyingSetsAll
    lock_frame_selection_to_range: BoolProperty()
    node_tree: PointerProperty(type=NodeTree)
    # objects: TODO https://docs.blender.org/api/current/bpy.types.SceneObjects.html#bpy.types.SceneObjects
    # render: TODO https://docs.blender.org/api/current/bpy.types.RenderSettings.html#bpy.types.RenderSettings
    # rigidbody_world: TODO https://docs.blender.org/api/current/bpy.types.RigidBodyWorld.html#bpy.types.RigidBodyWorld
    # safe_areas: TODO https://docs.blender.org/api/current/bpy.types.DisplaySafeAreas.html#bpy.types.DisplaySafeAreas
    # sequence_editor: TODO https://docs.blender.org/api/current/bpy.types.SequenceEditor.html#bpy.types.SequenceEditor
    # sequencer_colorspace_settings: TODO https://docs.blender.org/api/current/bpy.types.ColorManagedSequencerColorspaceSettings.html#bpy.types.ColorManagedSequencerColorspaceSettings
    show_keys_from_selected_only: BoolProperty()
    show_subframe: BoolProperty()
    sync_mode: StringProperty()
    # timeline_markers: TODO https://docs.blender.org/api/current/bpy.types.TimelineMarkers.html#bpy.types.TimelineMarkers
    # tool_settings: TODO https://docs.blender.org/api/current/bpy.types.ToolSettings.html#bpy.types.ToolSettings
    # transform_orientation_slots: TODO collection of https://docs.blender.org/api/current/bpy.types.TransformOrientationSlot.html#bpy.types.TransformOrientationSlot
    # unit_settings: TODO https://docs.blender.org/api/current/bpy.types.UnitSettings.html#bpy.types.UnitSettings
    use_audio: BoolProperty()
    use_audio_scrub: BoolProperty()
    use_gravity: BoolProperty()
    use_nodes: BoolProperty()
    use_preview_range: BoolProperty()
    use_stamp_note: StringProperty()
    # view_layers:  TODO https://docs.blender.org/api/current/bpy.types.ViewLayers.html#bpy.types.ViewLayers
    # view_settings: TODO https://docs.blender.org/api/current/bpy.types.ColorManagedViewSettings.html#bpy.types.ColorManagedViewSettings
    world: PointerProperty(type=World)
