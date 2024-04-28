class Game:
    def __init__(self):
        self._game_mode = "NOFORCEJUMP"
        self._over = False

    def force_jump(self):
        self._game_mode = "FORCEJUMP"