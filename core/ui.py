import bpy


def draw_store_list(layout, context, store_name):
    store = context.scene.sva.get_store(store_name)
    layout.template_list("SVA_UL_template_list", "", store, "store", store, "index")

    active_index = store.index

    row = layout.row(align=True)
    add = row.operator("sva.add_entry", text="Add", icon="ADD")
    add.container = store_name

    is_there_any_selected_entry = bool(store) and active_index >= 0
    sub_row = row.row(align=True)
    rem = sub_row.operator("sva.remove_entry", text="Remove", icon="REMOVE")
    rem.index = active_index
    rem.container = store_name
    sub_row.enabled = is_there_any_selected_entry

    ops = layout.row(align=True)
    store = ops.operator("sva.store_entry", text="Store", icon="COPYDOWN")
    store.container = store_name
    store.index = active_index
    restore = ops.operator("sva.restore_entry", text="Restore", icon="PASTEDOWN")
    restore.container = store_name
    restore.index = active_index
    ops.enabled = is_there_any_selected_entry



class SVA_UL_template_list(bpy.types.UIList):
    #   flt_flag is the result of the filtering process for this item.
    #   Note: as index and flt_flag are optional arguments, you do not have to use/declare them here if you don't
    #         need them.
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        row = layout.row()

        if self.layout_type in {"DEFAULT", "COMPACT"}:
            row.prop(item, "name", text="", emboss=False)
            
            sync = layout.operator("sva.store_entry_sync_settings", icon="OPTIONS", text="")
            sync.container = active_data.name
            sync.index = active_data.get_index(item)
        elif self.layout_type in {"GRID"}:
            layout.label(text=item.name)
