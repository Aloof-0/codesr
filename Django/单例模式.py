class A(object):
    __instance = 1
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance=object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

print(A())