import bpy
from stored_views_advanced.core.prop import StoreType


class MATERIAL_UL_matslots_example(bpy.types.UIList):
    #   flt_flag is the result of the filtering process for this item.
    #   Note: as index and flt_flag are optional arguments, you do not have to use/declare them here if you don't
    #         need them.
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        row = layout.row()

        if self.layout_type in {"DEFAULT", "COMPACT"}:
            row.prop(item, "name", text="", emboss=False)
            if item == active_data.active:
                row.popover("SVA_PT_store_entry_sync_settings", text="", icon="OPTIONS")
        elif self.layout_type in {"GRID"}:
            layout.label(text=item.name)


class SVA_PT_store_entry_sync_settings(bpy.types.Panel):
    bl_label = "Synch Settings"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "View"
    bl_options = {"INSTANCED"}

    def draw(self, context):
        layout = self.layout
        store = context.scene.sva.store_global

        sync = layout.row(align=True)
        sync_settings = store.active.sync_settings
        sync.label(text="Synchronize")
        sync.prop(sync_settings, "outliner", text="", icon="OUTLINER")
        sync.prop(sync_settings, "objects", text="", icon="OBJECT_DATAMODE")
        sync.prop(sync_settings, "view_layers", text="", icon="RENDERLAYERS")
        sync.prop(sync_settings, "collections", text="", icon="OUTLINER_COLLECTION")
        sync.prop(sync_settings, "viewport", text="", icon="VIEW3D")
        sync.prop(sync_settings, "shading", text="", icon="SHADING_RENDERED")
        sync.prop(sync_settings, "overlays", text="", icon="OVERLAY")


class SVA_PT_viewport(bpy.types.Panel):
    bl_label = "Stored Views Advanced"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "View"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout

        layout.template_list(
            "MATERIAL_UL_matslots_example",
            "",
            context.scene.sva.store_global,
            "store",
            context.scene.sva.store_global,
            "index",
        )

        active_index = context.scene.sva.store_global.index

        row = layout.row(align=True)
        add = row.operator("sva.add_entry", text="Add", icon="ADD")
        add.container = StoreType.GLOBAL.value

        is_there_any_selected_entry = bool(context.scene.sva.store_global) and active_index >= 0
        sub_row = row.row(align=True)
        rem = sub_row.operator("sva.remove_entry", text="Remove", icon="REMOVE")
        rem.index = active_index
        rem.container = StoreType.GLOBAL.value
        sub_row.enabled = is_there_any_selected_entry

        ops = layout.row(align=True)
        store = ops.operator("sva.store_entry", text="Store", icon="COPYDOWN")
        store.container = StoreType.GLOBAL.value
        store.index = active_index
        restore = ops.operator("sva.restore_entry", text="Restore", icon="PASTEDOWN")
        restore.container = StoreType.GLOBAL.value
        restore.index = active_index
        ops.enabled = is_there_any_selected_entry
