class Node:
    def __init__(self, data):
        self.__data = data
        self.__left = None
        self.__right = None

    @property
    def data(self):
        return self.__data

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right

    @data.setter
    def data(self, novo_dado):
        self.__data = novo_dado

    @left.setter
    def left(self, novo_dado):
        self.__left = novo_dado

    @right.setter
    def right(self, novo_dado):
        self.__right = novo_dado

    def __str__(self):
        return str(self.data)
