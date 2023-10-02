import typing


class Corge:
    __foo: typing.Any

    def __init__(self, foo):
        self.__foo = foo

    def setFoo(self, foo):
        self.__foo = foo
        if self.__foo.getCorge() != self:
            self.__foo.setCorge(self)
