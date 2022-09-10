import constant
import background
import pygame
import draw_game
import setup
import rules
import conversions


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

                                    selected_piece = p

                                    bg.x = p.get_mask_rect().x
                                    bg.y = p.get_mask_rect().y
                                    bg.selected = True

                                    move_options = rules.check_moves(pieces, p.pos[0], p.pos[1])
                                    if len(move_options) > 0:
                                        bg.can_move = True
                                        bg.move_list = move_options


                                else:
                                    bg.selected = False
                                    bg.can_move = False

                        elif bg.can_move == True:
                            for m in move_options:
                                print(m)
                                rect = pygame.Rect(constant.POS_LIST[m[0]][m[1]][0], constant.POS_LIST[m[0]][m[1]][1], bg.width, bg.height)
                                if rect.collidepoint(x, y):
                                    print(x, y)
                                    pieces = bg.move(pieces, selected_piece, m)
                                    bg.can_move = False
                                    bg.selected = False
                                    
                            

                                
        draw_game.draw_window(win, bg, pieces)

    
    pygame.quit()
    quit()

main()