from ipythonblocks import BlockGrid
from IPython.display import clear_output
import time


SCREEN_ROWS = 7
SCREEN_COLS = 5


colors = {
  'black': (0,0,0), 
  'white': (255, 255, 255),
  'red': (255, 0, 0),
  'yellow': (255, 255, 0),
}


black = colors['black']
red = colors['red']


screen = BlockGrid(SCREEN_COLS, SCREEN_ROWS, fill=black)


def erase(screen, color=black):
    screen[:, :] = color


def draw_1(color=red):
    screen = BlockGrid(SCREEN_COLS, SCREEN_ROWS, fill=black)
    screen[1, 1] = color
    screen[0, 2] = color
    screen[1, 2] = color
    screen[2, 2] = color
    screen[3, 2] = color
    screen[4, 2] = color
    screen[5, 2] = color
    screen[6, 2] = color
    screen[6, 1] = color
    screen[6, 3] = color
    return screen
    
    

digits = {
    'one': [ (1, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (6, 1), (6, 3) ],
    'two': [ (1, 0), (0, 1), (0, 2), (0, 3), (1, 4), (2, 4), (3, 3), (3, 2), (4, 1), (5, 0), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4)],
    'three': [ (1, 0), (0, 1), (0, 2), (0, 3), (1, 4), (2, 4), (3, 3), (3, 2), (3, 1), (4, 4), (5, 4), (5, 0), (6, 1), (6, 2), (6, 3) ]

}


def draw_points(points, color=red):
    screen = BlockGrid(SCREEN_COLS, SCREEN_ROWS, fill=black)
    for p in points:
        r = p[0]
        c = p[1]
        if  0 <= r < screen.height and 0 <= c < screen.width:
            screen[r, c] = color
    return screen


    
def shift(points, by_rows, by_cols):
    new_points = []
    for p in points:
        new_row = p[0] + by_rows
        new_col = p[1] + by_cols
        new_points.append((new_row, new_col))
    return new_points



def chess_board(n_rows=8, n_cols=8, fg=None, bg=None):
    if not bg:
        bg = colors['black']
    if not fg:
        fg = colors['yellow']

    screen = BlockGrid(n_cols, n_rows, fill=bg)
    for row in range(n_rows):
        for col in range(n_cols):
            if (row + col) % 2 == 0:
                screen[row, col] = fg
    return screen


def swiss_flag(n_rows=10, n_cols=10):
    red = (255, 0, 0)
    white = (255, 255, 255)
    
    screen = BlockGrid(n_cols, n_rows, fill=(255, 0, 0))
    screen.lines_on = False
    screen[2:8, 4:6] = white
    screen[4:6, 2:8] = white
    return screen
