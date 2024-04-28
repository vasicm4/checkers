from Constants import *


class Square:
    def __init__(self, file: str, rank: int) -> None:
        self._file = file
        self._rank = rank
        # self._square = (size,size)
        self._color = (240, 217, 181)

    def __str__(self) -> str:
        return "Field: " + self.file + str(self.rank)

    def __eq__(self, other) -> bool:
        return self.file == other.file and self.rank == other.rank

    def __iter__(self):
        return iter([self.file, self.rank])

#implement find square method

    @property
    def file(self) -> str:
        return self.file

    @property
    def rank(self) -> int:
        return self.rank

    @property
    def square(self) -> tuple:
        return self.square

    @file.setter
    def file(self, file):
        self.file = file

    @rank.setter
    def rank(self, rank):
        self.rank = rank

    @square.setter
    def square(self, size):
        self.square = (size, size)
