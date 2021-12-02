import bpy


class PropsStore:
    def store(self, copy_from):
        for prop in self.__annotations__:
            try:
                setattr(self, prop, getattr(copy_from, prop))
            except AttributeError:
                pass

    def restore(self, copy_to):
        for prop in self.__annotations__:
            try:
                setattr(copy_to, prop, getattr(self, prop))
            except AttributeError:
                pass
