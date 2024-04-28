from enum import Enum

WIDTH = 800
HEIGHT = WIDTH
CELL = WIDTH//8
FILES = [chr(i) for i in range(ord('a'), ord('i') + 1)]
RANKS = [i for i in range(1,9)]