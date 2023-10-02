from bar import Bar
from baz import Baz
from qux import Qux


class Foo:
    __bar: Bar
    __bazs: [Baz]
    __qux: Qux

    def __init__(self, bar: Bar):
        self.__bar = bar
        self.__bazs = []
        self.__qux = Qux()

    def getBar(self) -> Bar:
        return self.__bar

    def setBar(self, bar: Bar):
        self.__bar = bar

    def addBaz(self, baz: Baz):
        self.__bazs.append(baz)

    def removeBaz(self, baz: Baz):
        self.__bazs.remove(baz)

    def countBaz(self) -> int:
        return len(self.__bazs)

    def getBaz(self, index: int):
        if index < self.countBaz():
            return self.__bazs[index]
        else:
            return None

    def getQux(self) -> Qux:
        return self.__qux
