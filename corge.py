from foo import Foo


class Corge:
    __foo: Foo

    def __init__(self, foo: Foo):
        self.__foo = foo

    def setFoo(self, foo: Foo):
        self.__foo = foo
        if self.__foo.getCorge() != self:
            self.__foo.setCorge(self)
