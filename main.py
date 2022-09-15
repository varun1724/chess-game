import constant
import background
import pygame
from conversions import pixels_to_list
import draw_game
import setup
import rules


def main():

    bg = background.Background(constant.WIN_WIDTH, constant.WIN_HEIGHT)
    pieces = setup.setup_board()

    win = pygame.display.set_mode((constant.WIN_WIDTH, constant.WIN_HEIGHT))
    clock = pygame.time.Clock()

    run = True
    white_turn = True
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

                                    if (white_turn and p.team == 'w') or (not white_turn and p.team == 'b'):

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
                                            if selected_piece.type == 'k' and selected_piece.can_castle == True:
                                                if rect.x == selected_piece.pos[0] + 200:
                                                    pieces = rules.move(pieces, pieces[m[0]][7], (m[0], 5))
                                                elif rect.x == selected_piece.pos[0] - 200:
                                                    pieces = rules.move(pieces, pieces[m[0]][0], (m[0], 3))
                                                selected_piece.can_castle = False
                                            elif selected_piece.type == 'r':
                                                selected_piece.can_castle = False
                                            pieces = rules.move(pieces, selected_piece, m)
                                            white_turn = not white_turn
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
                                    if selected_piece.type == 'k' and selected_piece.can_castle == True:
                                        if rect.x == selected_piece.pos[0] + 200:
                                            pieces = rules.move(pieces, pieces[m[0]][7], (m[0], 5))
                                        elif rect.x == selected_piece.pos[0] - 200:
                                            pieces = rules.move(pieces, pieces[m[0]][0], (m[0], 3))
                                        selected_piece.can_castle = False
                                    elif selected_piece.type == 'r':
                                        selected_piece.can_castle = False
                                    pieces = rules.move(pieces, selected_piece, m)
                                    white_turn = not white_turn
                                    bg.can_move = False
                                    bg.selected = False
                                    just_moved = True
                                    
        draw_game.draw_window(win, bg, pieces)

    
    pygame.quit()
    quit()

main()