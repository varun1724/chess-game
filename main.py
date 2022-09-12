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

    just_moved = False

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
                                # print("ran1")
                                if bg.selected == False and not just_moved:
                                    # print("Case 1")

                                    selected_piece = p

                                    bg.x = p.get_mask_rect().x
                                    bg.y = p.get_mask_rect().y
                                    bg.selected = True

                                    move_options = rules.check_moves(pieces, p.pos[0], p.pos[1])
                                    if len(move_options) > 0:
                                        bg.can_move = True
                                        bg.move_list = move_options

                                elif bg.can_move == True:
                                    # print("case 2")
                                    is_movable_spot = False
                                    for m in move_options:
                                        rect = pygame.Rect(constant.POS_LIST[m[0]][m[1]][0], constant.POS_LIST[m[0]][m[1]][1], bg.width, bg.height)
                                        if rect.collidepoint(x, y):
                                            pieces = bg.move(pieces, selected_piece, m)
                                            bg.can_move = False
                                            bg.selected = False
                                            is_movable_spot = True
                                    if not is_movable_spot:
                                        bg.selected = False
                                        bg.can_move = False

                                else:
                                    # print("case 3")
                                    bg.selected = False
                                    bg.can_move = False
                                    just_moved = False

                        elif bg.can_move == True:
                            # print("case 4")
                            for m in move_options:
                                rect = pygame.Rect(constant.POS_LIST[m[0]][m[1]][0], constant.POS_LIST[m[0]][m[1]][1], bg.width, bg.height)
                                if rect.collidepoint(x, y):
                                    pieces = bg.move(pieces, selected_piece, m)
                                    bg.can_move = False
                                    bg.selected = False
                                    just_moved = True
                                    
                            

                                
        draw_game.draw_window(win, bg, pieces)

    
    pygame.quit()
    quit()

main()