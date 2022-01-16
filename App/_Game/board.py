
from .settings import BLANK
from .player import Player


class Board:
    def __init__(self):
        self.tiles = [BLANK for _ in range(9)]

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__ = state

    def reset(self):
        self.tiles = [BLANK for _ in range(9)]

    def set_move(self, player: Player, tile_ndx: int) -> None:
        self.tiles[tile_ndx] = player.color

    def get_tile_color(self, tile_ndx: int) -> tuple:
        return self.tiles[tile_ndx]
