import pygame
import constant

def draw_window(win, background, board, checkmate):

    background.draw(win)

    if not checkmate:
        text = constant.BASE_FONT.render("Promotion keys -- 1: Queen   2: Knight   3: Rook   4: Bishop", 1, (0, 0, 0))
        win.blit(text, (5, 810))
    else:
        text = constant.BASE_FONT.render("Promotion keys -- 1: Queen   2: Knight   3: Rook   4: Bishop     Checkmate", 1, (0, 0, 0))
        win.blit(text, (5, 810))

    for row in board:
        for p in row:
            if p != ' ':
                p.draw(win)

    pygame.display.update()