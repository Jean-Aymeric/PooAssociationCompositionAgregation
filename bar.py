class Bar:
    __name: str

    def __init__(self, name: str):
        self.__name = name

    def getName(self) -> str:
        return self.__name
