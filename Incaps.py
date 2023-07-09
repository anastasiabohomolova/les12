class Incapsyl:
    def __init__(self, x, y, z):
        self.x = x
        self._y = y
        self.__z = z

    def one(self):
        return self.x

    def _two(self):
        print(self._y)

    @property
    def three(self):
        return self.__z

    @three.setter
    def three(self, arg):
        self.__z = arg

    @three.deleter
    def three(self):
        del self.__z





