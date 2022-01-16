from math import inf

from .settings import P1_COLOR, P2_COLOR, BLANK, HUMAN, COMP, NIL, DRAW
from .player import Player, wins_by_color
from .board import Board


class Game:
    def __init__(self, first: int):
        self.players = {
            HUMAN: Player(P1_COLOR),
            COMP: Player(P2_COLOR)
        }
        self.moves = {
            HUMAN: [],
            COMP: []
        }
        self.wins = {
            HUMAN: 0,
            COMP: 0
        }
        self.board = Board()
        self.first = first
        self.turn = first

    def __getstate__(self):
        del self.board
        del self.players
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__ = state
        self.board = Board()
        self.players = {
            HUMAN: Player(P1_COLOR),
            COMP: Player(P2_COLOR)
        }
        self.re_apply_moves()

    def update(self, player_ndx: int, tile_ndx: int = inf) -> int:
        if tile_ndx == -1:
            print("Not a valid move, waiting for new move...")
            return NIL
        if self.turn != player_ndx:
            return NIL
        if self.turn == HUMAN and self.turn == player_ndx:
            self.set_move(HUMAN, tile_ndx)
            print(f"Player {player_ndx}'s turn, playing at tile {tile_ndx}...")
        if self.turn == COMP and self.turn == player_ndx:
            ai_move = self.players[COMP].get_ai_move(self.board.tiles)
            self.set_move(COMP, ai_move)
            print(f"Player {player_ndx}'s turn, playing at tile {ai_move}...")
        winner = self.check_win(self.players[player_ndx].get_color())
        if winner is not NIL and winner is not DRAW:
            self.wins[winner] += 1
        return winner

    def reset(self):
        self.board.reset()
        self.moves[HUMAN].clear()
        self.moves[COMP].clear()
        self.turn = self.first

    def check_win(self, color: tuple) -> int:
        return wins_by_color(self.get_tile_colors(), color)

    def set_move(self, player_ndx: int, tile_ndx: int) -> None:
        if self.board.tiles[tile_ndx] != BLANK:
            return
        self.moves[player_ndx].append(tile_ndx)
        print(self.moves)
        self.board.set_move(self.players[player_ndx], tile_ndx)
        self.turn = HUMAN if self.turn == COMP else COMP

    def re_apply_moves(self):
        for key in self.moves.keys():
            for move in self.moves[key]:
                self.board.set_move(self.players[key], move)

    def get_tile_colors(self) -> list:
        return self.board.tiles

    def get_wins(self):
        return self.wins
