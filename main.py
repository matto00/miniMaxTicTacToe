
import tkinter as tk


intToRC = {
    0: (0, 0), 1: (0, 1), 2: (0, 2),
    3: (1, 0), 4: (1, 1), 5: (1, 2),
    6: (2, 0), 7: (2, 1), 8: (2, 2)
}


def getMark(turn):
    if turn == 0:
        return 'x'
    return 'o'


class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player(0), AI(1)]

    def run(self):
        turn = 0
        running = True
        while running:
            move = self.getMove(turn)
            self.board.mark(move, turn)

    def getMove(self, turn):
        return self.players[turn].getMove()


class Player:
    def __init__(self, turn):
        self.turn = turn
        self.mark = getMark(turn)

    def getMove(self):
        # return move in form i, j
        intMove = int(input("Enter a move:\n"))
        move = intToRC[intMove]
        return 0, 0


class AI (Player):
    def __init__(self, turn):
        super().__init__(turn)

    def getMove(self):
        # return move in form i, j
        return 0, 0


class Board:
    def __init__(self):
        self.tiles = [[Tile(i, j) for i in range(3)] for j in range(3)]

    def __str__(self):
        s = ''
        for row in self.tiles:
            s += ' '
            for col in row:
                s += col.mark
                if col is not row[-1]:
                    s += ' | '
            if row is not self.tiles[-1]:
                s += '\n---|---|---'
            s += '\n'

        return s

    def mark(self, move, turn):
        self.tiles[move[0]][move[1]].mark = getMark(turn)


class Tile:
    def __init__(self, i, j):
        self.row = i
        self.col = j
        self.mark = '/'


def main():
    game = Game()
    game.run()


main()
