import bpy
from .constant import SETTINGS_TYPES, ICONS


def draw_id(layout, context, store_name):
    if not context.scene.sva.stores:
        layout.operator("sva.init_stores")
        return
    store = context.scene.sva.get(store_name)
    current_item = None
    current_entry = None
    if hasattr(context, store_name):
        current_item = getattr(context, store_name)
        current_entry = store.get(current_item)
    current_index = store.get_index(current_entry) if current_entry else -1

    row = layout.row(align=True)
    if current_entry:
        store = row.operator("sva.store_entry", text="Store", icon="COPYDOWN")
        store.store = store_name
        store.index = current_index
        store.is_storing = True
    else:
        add = row.operator("sva.add_entry", text="Store", icon="COPYDOWN")
        add.store = store_name
        if current_item:
            add.name = current_item.name

    restore_row = row.row(align=True)
    restore = restore_row.operator("sva.store_entry", icon="PASTEDOWN", text="Restore")
    restore.store = store_name
    restore.index = current_index
    restore.is_storing = False
    restore_row.enabled = bool(current_entry)

    sync_row = row.row(align=True)
    sync = sync_row.operator("sva.store_entry_sync_settings", icon="OPTIONS", text="")
    sync.store = store_name
    sync.index = current_index
    sync_row.enabled = current_index >= 0


def draw_store_list(layout, context, store_name):
    if not context.scene.sva.stores:
        layout.operator("sva.init_stores")
        return
    store = context.scene.sva.get(store_name)

    layout.template_list("SVA_UL_template_list", "", store, "store", store, "index")

    row = layout.row(align=True)
    add = row.operator("sva.add_entry", text="New View", icon="ADD")
    add.store = store_name

    inspect = row.row(align=True)
    inspect.enabled = store.active is not None
    inspect.prop(context.scene.sva, "inspect", text="", icon="VIEWZOOM")
    if context.scene.sva.inspect and store.active is not None:
        entry = store.active
        for prop_name in SETTINGS_TYPES:
            if not getattr(entry.sync_settings, prop_name) or not getattr(entry.stored_props, prop_name):
                continue
            box = layout.box()
            box.label(text=prop_name.title().replace("_", " "), icon=ICONS.get(prop_name, "BLANK1"))
            prop = getattr(entry, prop_name)
            if hasattr(prop, "__annotations__"):
                for ann in prop.__annotations__:
                    box.prop(getattr(entry, prop_name), ann)
            else:
                for sub_prop in prop:
                    sub_box = box.box()
                    sub_box.label(text=sub_prop.name)
                    for ann in sub_prop.__annotations__:
                        try:
                            for sub_sub_prop in getattr(sub_prop, ann):
                                if hasattr(sub_sub_prop, "__annotations__"):
                                    for ann in sub_sub_prop.__annotations__:
                                        sub_box.prop(sub_sub_prop, ann)
                        except TypeError:
                            sub_box.prop(sub_prop, ann)

class SVA_UL_template_list(bpy.types.UIList):
    #   flt_flag is the result of the filtering process for this item.
    #   Note: as index and flt_flag are optional arguments, you do not have to use/declare them here if you don't
    #         need them.
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        row = layout.row(align=True)
        store_name = active_data.name
        active_index = active_data.get_index(item)

        if self.layout_type in {"DEFAULT", "COMPACT"}:
            row.prop(item, "name", text="", emboss=False)

            store = row.operator("sva.store_entry", text="", icon="COPYDOWN")
            store.store = store_name
            store.index = active_index
            store.is_storing = True

            restore = row.operator("sva.store_entry", text="", icon="PASTEDOWN")
            restore.store = store_name
            restore.index = active_index
            restore.is_storing = False

            sync = row.operator("sva.store_entry_sync_settings", icon="OPTIONS", text="")
            sync.store = store_name
            sync.index = active_index

            remove = row.operator("sva.remove_entry", text="", icon="REMOVE")
            remove.store = store_name
            remove.index = active_index
        elif self.layout_type in {"GRID"}:
            layout.label(text=item.name)
