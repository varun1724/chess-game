import constant
import background
import pygame
from conversions import pixels_to_list
import draw_game
import setup
import rules
import piece


def main():

    bg = background.Background(constant.WIN_WIDTH, constant.WIN_HEIGHT)
    pieces = setup.setup_board()

    win = pygame.display.set_mode((constant.WIN_WIDTH, constant.WIN_HEIGHT))
    clock = pygame.time.Clock()

    run = True
    white_turn = True
    just_moved = False
    checkmate = False
    promotion = False

    while run:

        clock.tick(20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif pygame.key.get_pressed()[pygame.K_1] and promotion and not checkmate:
                print("queen")
                promotion_piece(pieces, 'q')
                promotion = False
            elif pygame.key.get_pressed()[pygame.K_2] and promotion and not checkmate:
                promotion_piece(pieces, 'n')
                promotion = False
            elif pygame.key.get_pressed()[pygame.K_3] and promotion and not checkmate:
                promotion_piece(pieces, 'r')
                promotion = False
            elif pygame.key.get_pressed()[pygame.K_4] and promotion and not checkmate:
                promotion_piece(pieces, 'b')
                promotion = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not checkmate and not promotion:
                x, y = event.pos
                for rows in pieces:
                    for p in rows:
                        if p != ' ':
                            if p.get_mask_rect().collidepoint(x, y):
                                if bg.selected == False and not just_moved:

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
                                    if check_promotion(pieces):
                                        print("promotion true 1")
                                        promotion = True
                                    if check_mate(pieces, selected_piece):
                                        checkmate = True
                                    if not is_movable_spot:
                                        bg.selected = False
                                        bg.can_move = False

                                else:
                                    bg.selected = False
                                    bg.can_move = False
                                    just_moved = False

                        elif bg.can_move == True:
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
                            if check_promotion(pieces):
                                promotion = True
                                print("promotion true 2")
                            if check_mate(pieces, selected_piece):
                                checkmate = True
                                    
        draw_game.draw_window(win, bg, pieces, checkmate)
    
    pygame.quit()
    quit()



def check_mate(pieces, selected_piece):
    a, b = pixels_to_list(selected_piece.pos[0], selected_piece.pos[1])
    if rules.in_check(pieces, a, b, True) == True:
        for row in pieces:
            for p in row:
                if p != ' ' and p.team != pieces[a][b].team and p.type == 'k':
                    c, d = pixels_to_list(p.pos[0], p.pos[1])
                    break
        if rules.check_king(pieces, c, d) == "mate":
            return True

    return False


def check_promotion(pieces):

    for r in range(0, 8):
        if pieces[0][r] != ' ' and pieces[0][r].type == 'p':
            return True
        elif pieces[0][r] != ' ' and pieces[7][r] == 'p':
            return True
    
    return False


def promotion_piece(pieces, type):

    a, b = 0, 0 

    for r in range(0, 8):
        if pieces[0][r] != ' ' and pieces[0][r].type == 'p':
            selected_piece = pieces[0][r]
            b = r
            break
        elif pieces[0][r] != ' ' and pieces[7][r] == 'p':
            selected_piece = pieces[7][r]
            a = 7
            b = r
            break

    if type == 'q':
        if selected_piece.team == 'w':
            pieces[a][b] = piece.Piece(selected_piece.team, 'q', constant.PIECE_IMGS[10], selected_piece.pos)
        else:
            pieces[a][b] = piece.Piece(selected_piece.team, 'q', constant.PIECE_IMGS[3], selected_piece.pos)
    elif type == 'n':
        if selected_piece.team == 'w':
            pieces[a][b] = piece.Piece(selected_piece.team, 'n', constant.PIECE_IMGS[8], selected_piece.pos)
        else:
            pieces[a][b] = piece.Piece(selected_piece.team, 'n', constant.PIECE_IMGS[1], selected_piece.pos)
    elif type == 'r':
        if selected_piece.team == 'w':
            pieces[a][b] = piece.Piece(selected_piece.team, 'r', constant.PIECE_IMGS[7], selected_piece.pos)
        else:
            pieces[a][b] = piece.Piece(selected_piece.team, 'r', constant.PIECE_IMGS[0], selected_piece.pos)
    elif type == 'b':
        if selected_piece.team == 'w':
            pieces[a][b] = piece.Piece(selected_piece.team, 'b', constant.PIECE_IMGS[9], selected_piece.pos)
        else:
            pieces[a][b] = piece.Piece(selected_piece.team, 'b', constant.PIECE_IMGS[2], selected_piece.pos)


main()