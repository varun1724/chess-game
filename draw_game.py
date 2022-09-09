import pygame

def draw_window(win, background, board):

    background.draw(win)

    for row in board:
        for p in row:
            if p != ' ':
                p.draw(win)

    pygame.display.update()