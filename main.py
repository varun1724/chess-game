import constant
import background
import pygame
import draw_game
import setup
import rules


def main():

    bg = background.Background(constant.WIN_WIDTH, constant.WIN_HEIGHT)
    pieces = setup.setup_board()

    win = pygame.display.set_mode((constant.WIN_WIDTH, constant.WIN_HEIGHT))
    clock = pygame.time.Clock()

    run = True

    while run:

        clock.tick(20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for rows in pieces:
                    for p in rows:
                        if p != ' ':
                            if p.get_mask_rect().collidepoint(x, y):
                                if bg.selected == False:
                                    bg.set_x(p.get_mask_rect().x)
                                    bg.set_y(p.get_mask_rect().y)
                                    bg.set_selected(True)

                                    move_options = rules.check_moves(pieces, p.pos[0], p.pos[1])
                                    print(move_options)
                                    if len(move_options) > 0:
                                        bg.set_move_state(True)
                                        bg.set_move_list(move_options)


                                else:
                                    bg.set_selected(False)
                                    bg.set_move_state(False)
                                






        draw_game.draw_window(win, bg, pieces)

    
    pygame.quit()
    quit()

main()