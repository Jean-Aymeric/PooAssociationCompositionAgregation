from bar import Bar


class Foo:
    __bar: Bar

    def __init__(self, bar: Bar):
        self.__bar = bar

    def getBar(self) -> Bar:
        return self.__bar

    def setBar(self, bar: Bar):
        self.__bar = bar
