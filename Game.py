class Game:
    def __init__(self, forcejump: bool = False) -> None:
        self._force_jump = forcejump
        self._over = False

    def force_jump(self):
        self._game_mode = "FORCEJUMP"