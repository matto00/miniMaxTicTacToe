import pygame
from time import sleep
import pickle
import os

from ._Game.game import Game
from ._Game.player import color_from_ndx
from ._Game.settings import *


def clear_console():
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')


class Application:
    def __init__(self, config):
        self.init_pygame()
        self.game = None
        if config["has_save_state"]:
            self.load_state()
        else:
            self.game = Game(config["first"])
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.font = pygame.font.SysFont(FONT, 20)
        self.dynamic_objs = self.init_dynamic_objs()
        self.static_objs = self.init_static_objs()
        clear_console()

    @staticmethod
    def init_pygame() -> None:
        print("Initializing pygame and its utilities...")
        pygame.init()
        pygame.display.init()
        pygame.display.set_caption("TicTacToe.py")
        pygame.font.init()
        print(TermColors.OKGREEN + "Initialization complete" + TermColors.ENDC)

    def init_dynamic_objs(self) -> dict:
        print("Initializing dynamic objects...")
        objects = {
            "tiles": [],
            "win_counts": []
        }
        print("Initializing tiles...")
        for i in range(3):
            for j in range(3):
                left = WIDTH * 0.05 + (TILE_WIDTH * j) + (j * 5)
                top = (HEIGHT / 4) + (HEIGHT * 0.05) + (TILE_HEIGHT * i) + (i * 5)
                objects["tiles"].append(pygame.Rect(left, top, TILE_WIDTH, TILE_HEIGHT))
        print("Initializing win counts...")
        self.update_win_count(objects)
        print(TermColors.OKGREEN + "Initialization complete" + TermColors.ENDC)
        return objects

    def init_static_objs(self) -> dict:
        print("Initializing static objects...")
        objects = {
            "labels": [self.font.render("Tic Tac Toe", False, TEXT_COLOR, BG_COLOR)]
        }
        print(TermColors.OKGREEN + "Initialization complete" + TermColors.ENDC)
        return objects

    def deconstruct(self) -> None:
        print("Closing application...")
        self.save_state()
        print(TermColors.BOLD + TermColors.WARNING + "Deconstructing application..." + TermColors.ENDC)
        pygame.font.quit()
        pygame.display.quit()
        pygame.quit()
        print(TermColors.OKGREEN + "Deconstruction complete" + TermColors.ENDC)

    def save_state(self) -> None:
        if not self.config["save_game_state"]:
            return
        print("Saving game...")
        with open(SAVE_PATH, "wb") as f:
            pickle.dump(self.game, f)
            f.close()
        print(TermColors.OKGREEN + "_Game saved successfully" + TermColors.ENDC)

    def load_state(self) -> None:
        print("Loading saved game...")
        try:
            with open(LOAD_PATH, "rb") as f:
                self.game = pickle.load(f)
                f.close()
        except FileNotFoundError:
            print(TermColors.FAIL + f"Error: Could not find file \"{LOAD_PATH}\", loading new game..." +
                  TermColors.ENDC)
            self.game = Game(RUN_CONFIG["first"])
        print(TermColors.OKGREEN + "_Game loaded successfully" + TermColors.ENDC)

    def run(self) -> None:
        print(TermColors.HEADER + "Running application..." + TermColors.ENDC)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.K_q or event.type == pygame.K_ESCAPE:
                    self.deconstruct()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_event(event.type)
            self.update_display()

    def update_display(self) -> None:
        self.display.fill(BLACK)
        tile_colors = self.game.get_tile_colors()
        # Draw tiles
        for i in range(len(self.dynamic_objs["tiles"])):
            pygame.draw.rect(self.display, tile_colors[i], self.dynamic_objs["tiles"][i])
        # Draw win counts
        self.display.blit(self.dynamic_objs["win_counts"][0], P1_LABEL_POS)
        self.display.blit(self.dynamic_objs["win_counts"][1], P2_LABEL_POS)
        # Draw labels
        self.display.blit(self.static_objs["labels"][0], GAME_LABEL_POS)
        pygame.display.update()

    def handle_event(self, event: pygame.event) -> None:
        print(f"Handling event: {event}...")
        if event == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for obj in self.dynamic_objs["tiles"]:
                if obj.collidepoint(pos[0], pos[1]):
                    self.handle_move(self.dynamic_objs["tiles"].index(obj))
        print("Handling complete")

    def handle_move(self, tile_ndx: int) -> None:
        print(f"Handling move at ndx: {tile_ndx}")
        win_state = self.game.update(HUMAN, tile_ndx)
        self.update_display()
        if win_state is NIL:
            win_state = self.game.update(COMP)
            self.update_display()
        if win_state is not NIL:
            self.handle_win(win_state)
            self.update_display()

    def handle_win(self, win_state: int) -> None:
        self.display_winner(win_state)
        self.game.reset()

    def update_win_count(self, objects: dict = None) -> None:
        wins = self.game.get_wins()
        if objects is None:
            self.dynamic_objs["win_counts"] = [
                self.font.render("Player 1: " + str(wins[HUMAN]), False, TEXT_COLOR, BG_COLOR),
                self.font.render("Player 2: " + str(wins[COMP]), False, TEXT_COLOR, BG_COLOR)
            ]
        else:
            objects["win_counts"] = [
                self.font.render("Player 1: " + str(wins[HUMAN]), False, TEXT_COLOR, BG_COLOR),
                self.font.render("Player 2: " + str(wins[COMP]), False, TEXT_COLOR, BG_COLOR)
            ]

    def display_winner(self, winner: int) -> None:
        if winner is not DRAW:
            self.update_win_count()
            color = color_from_ndx(winner)
            winner_text = "Player 1" if winner is HUMAN else "Player 2"
            winner_text += " won!"
        else:
            winner_text = "Draw!"
            color = TEXT_COLOR
        text = self.font.render(winner_text, False, color, BG_COLOR)
        text_pos = ((WIDTH * 0.5) - ((len(winner_text) * FONT_SIZE) / 2), HEIGHT * 0.9)
        self.display.blit(text, text_pos)
        pygame.display.update()
        sleep(1)
