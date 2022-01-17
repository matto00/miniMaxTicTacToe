
# PyGame Constants
# 3:4 ratio
WIDTH = 600
HEIGHT = 1000
TILE_WIDTH = TILE_HEIGHT = 175
P1_LABEL_POS = (WIDTH * 0.1, HEIGHT * 0.1)
P2_LABEL_POS = (WIDTH * 0.75, HEIGHT * 0.1)
GAME_LABEL_POS = (WIDTH * 0.4, HEIGHT * 0.05)

MP_BUTTON_LEFT = WIDTH * 0.35
MP_BUTTON_TOP = HEIGHT * 0.6
MP_BUTTON_WIDTH = WIDTH * 0.3
MP_BUTTON_HEIGHT = HEIGHT * 0.05

NAME_TF_LEFT = WIDTH * 0.35
NAME_TF_TOP = HEIGHT * 0.4
NAME_TF_WIDTH = WIDTH * 0.3
NAME_TF_HEIGHT = HEIGHT * 0.05

PLAY_BTN_LEFT = WIDTH * 0.4
PLAY_BTN_TOP = HEIGHT * 0.7
PLAY_BTN_WIDTH = WIDTH * 0.2
PLAY_BTN_HEIGHT = HEIGHT * 0.05

# COLORS
RED = (255, 0, 0)
GREEN = (0, 255, 100)
BLUE = (0, 100, 255)
CYAN = (50, 150, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BG_COLOR = BLACK
TEXT_COLOR = WHITE
TF_COLOR = (50, 50, 50)
BLANK = WHITE

# Font Style
FONT = "Verdana"
FONT_SIZE = 20

# _Game Constants
HUMAN = +1
COMP = -1
# ALPHA/BETA apply to minimax evaluation function
ALPHA = +1  # Computer wins
BETA = -1  # Human wins
GAMMA = 0  # Draw
NIL = 0
DRAW = 2
P1_COLOR = BLUE
P2_COLOR = RED
RUN_CONFIG = {
    "save_game_state": True,
    "has_save_state": True,
    "first": HUMAN
}
LOAD_PATH = SAVE_PATH = "./gamesave.bin"


class TermColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
