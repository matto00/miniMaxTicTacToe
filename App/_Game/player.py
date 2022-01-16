from random import randint
from math import inf
from time import sleep

from .settings import P1_COLOR, P2_COLOR, BLANK, HUMAN, COMP, NIL, DRAW, TermColors


def wins_by_color(state: list, player_color: tuple) -> int:
    win_state = [[state[0], state[1], state[2]],
                 [state[3], state[4], state[5]],
                 [state[6], state[7], state[8]],
                 [state[0], state[3], state[6]],
                 [state[1], state[4], state[7]],
                 [state[2], state[5], state[8]],
                 [state[0], state[4], state[8]],
                 [state[2], state[4], state[6]]]
    if [player_color, player_color, player_color] in win_state:
        return ndx_from_color(player_color)
    no_blank = True
    for tile in state:
        if tile is BLANK:
            no_blank = False
            break
    if no_blank:
        return DRAW
    return NIL


def wins_by_ndx(state: list, player_ndx: int) -> bool:
    win_state = [[state[0], state[1], state[2]],
                 [state[3], state[4], state[5]],
                 [state[6], state[7], state[8]],
                 [state[0], state[3], state[6]],
                 [state[1], state[4], state[7]],
                 [state[2], state[5], state[8]],
                 [state[0], state[4], state[8]],
                 [state[2], state[4], state[6]]]
    if [player_ndx, player_ndx, player_ndx] in win_state:
        return True
    return False


def blank_tiles_by_ndx(state: list) -> list:
    blank = []
    for i in range(len(state)):
        if state[i] is NIL:
            blank.append(i)
    return blank


def game_over_by_ndx(state: list) -> bool:
    for tile in state:
        if tile is NIL:
            return False
    return True


def color_from_ndx(ndx: int) -> tuple:
    return P1_COLOR if ndx is HUMAN else P2_COLOR if ndx is COMP else BLANK


def ndx_from_color(color: tuple) -> int:
    return HUMAN if color is P1_COLOR else COMP if color is P2_COLOR else NIL


def convert_colors_to_ndxs(state: list) -> list:
    converted = []
    for color in state:
        converted.append(ndx_from_color(color))
    return converted


class Player:
    def __init__(self, color: tuple):
        self.color = color

    def get_color(self):
        return self.color

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__ = state

    def get_ai_move(self, tiles: list) -> int:
        print("Getting AI move...")
        state = convert_colors_to_ndxs(tiles)
        empty = blank_tiles_by_ndx(state)
        depth = len(empty)
        if depth == 0 or game_over_by_ndx(state):
            return -1
        if depth == 9:
            return randint(0, 9)
        print("Beginning minimax sequence...")
        minimax = self.minimax(state, depth, COMP)
        print(f"Optimal move has been found at tile {minimax}...")
        sleep(0.5)
        # sleep(0.25 * (9 / depth)) make it seem harder for computer as time goes on
        return minimax[0]

    def minimax(self, state: list, depth: int, player_ndx: int) -> list:
        if player_ndx == COMP:
            best = [-1, -inf]
        else:
            best = [-1, +inf]

        if depth == 0 or game_over_by_ndx(state):
            score = self.evaluate(state)
            return [-1, score]

        empty = blank_tiles_by_ndx(state)
        print(TermColors.HEADER + f"{depth} - {empty}" + TermColors.ENDC)
        for ndx in empty:
            state[ndx] = player_ndx
            score = self.minimax(state, depth - 1, -player_ndx)
            state[ndx] = NIL
            score[0] = ndx
            if player_ndx == COMP:
                if score[1] > best[1]:
                    best = score
            else:
                if score[1] < best[1]:
                    best = score
        return best

    @staticmethod
    def evaluate(state: list) -> int:
        return +1 if wins_by_ndx(state, COMP) else -10 if wins_by_ndx(state, HUMAN) else 0
