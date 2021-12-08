import bpy


class PropsStore:
    def store(self, copy_from):
        for prop in self.__annotations__:
            if prop == "sub_props_store":
                for sub_prop_name in getattr(self, prop):
                    sub_prop = getattr(self, sub_prop_name.name)
                    sub_prop.store(getattr(copy_from, sub_prop_name.name))
                continue
            try:
                setattr(self, prop, getattr(copy_from, prop))
            except AttributeError:
                pass

    def restore(self, copy_to):
        for prop in self.__annotations__:
            if prop == "sub_props_store":
                for sub_prop_name in getattr(self, prop):
                    sub_prop = getattr(self, sub_prop_name.name)
                    sub_prop.restore(getattr(copy_to, sub_prop_name.name))
                continue
            try:
                copy_from_value = getattr(self, prop)
                copy_to_value = getattr(copy_to, prop)
                if copy_to_value != copy_from_value:
                    setattr(copy_to, prop, copy_from_value)
            except AttributeError:
                pass

    def init(self):
        if hasattr(self, "sub_props_store"):
            self.sub_props_store.clear()
            for prop_name in self.__annotations__:
                prop = getattr(self, prop_name)
                if isinstance(prop, PropsStore):
                    new = self.sub_props_store.add()
                    new.name = prop_name


class StringPropertyGroup(bpy.types.PropertyGroup):
    pass
