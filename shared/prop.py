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
                copy_from_value = getattr(self, prop)
                copy_to_value = getattr(copy_to, prop)
                if copy_to_value != copy_from_value:
                    setattr(copy_to, prop, copy_from_value)
            except AttributeError:
                pass
