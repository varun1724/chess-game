from itertools import chain
import conversions
import setup
import constant

# Returns a list of x, y coords
def check_moves(pieces, x_coord, y_coord):

    x, y = conversions.pixels_to_list(x_coord, y_coord)
    
    if pieces[x][y].type == 'p':
        return check_pawn(pieces, x, y)
    elif pieces[x][y].type == 'r':
        return check_rook(pieces, x, y, False)
    elif pieces[x][y].type == 'n':
        return check_knight(pieces, x, y, False)
    elif pieces[x][y].type == 'b':
        return check_bishop(pieces, x, y, False)
    elif pieces[x][y].type == 'q':
        return check_queen(pieces, x, y, False)
    else:
        return check_king(pieces, x, y)


# Still need to code promotion and en pasant 
def check_pawn(pieces, x, y):

    spaces = []

    if pieces[x][y].team == 'w':
        if x > 0:
            if pieces[x-1][y] == ' ':
                pieces_copy = setup.setup_copy_board(pieces)
                pieces_copy = move(pieces_copy, pieces_copy[x][y], (x-1, y))
                if not in_check(pieces_copy, x-1, y):
                    spaces.append((x-1, y))
            if x == 6 and pieces[x-2][y] == ' ':
                pieces_copy = setup.setup_copy_board(pieces)
                pieces_copy = move(pieces_copy, pieces_copy[x][y], (x-2, y))
                if not in_check(pieces_copy, x-2, y):
                    spaces.append((x-2, y))
            if y < 7:
                if pieces[x-1][y+1] != ' ' and pieces[x-1][y+1].type != 'k' and pieces[x-1][y+1].team != 'w':
                    pieces_copy = setup.setup_copy_board(pieces)
                    pieces_copy = move(pieces_copy, pieces_copy[x][y], (x-1, y+1))
                    if not in_check(pieces_copy, x-1, y+1):
                        spaces.append((x-1, y+1))
            if y > 0:
                if pieces[x-1][y-1] != ' ' and pieces[x-1][y-1].type != 'k' and pieces[x-1][y-1].team != 'w':
                    pieces_copy = setup.setup_copy_board(pieces)
                    pieces_copy = move(pieces_copy, pieces_copy[x][y], (x-1, y-1))
                    if not in_check(pieces_copy, x-1, y-1):
                        spaces.append((x-1, y-1))
    else:
        if x < 7:
            if pieces[x+1][y] == ' ':
                pieces_copy = setup.setup_copy_board(pieces)
                pieces_copy = move(pieces_copy, pieces_copy[x][y], (x+1, y))
                if not in_check(pieces_copy, x+1, y):
                    spaces.append((x+1, y))
            if x == 1 and pieces[x+2][y] == ' ':
                pieces_copy = setup.setup_copy_board(pieces)
                pieces_copy = move(pieces_copy, pieces_copy[x][y], (x+2, y))
                if not in_check(pieces_copy, x+2, y):
                    spaces.append((x+2, y))
            if y < 7:
                if pieces[x+1][y+1] != ' ' and pieces[x+1][y+1].type != 'k' and pieces[x+1][y+1].team != 'b':
                    pieces_copy = setup.setup_copy_board(pieces)
                    pieces_copy = move(pieces_copy, pieces_copy[x][y], (x+1, y+1))
                    if not in_check(pieces_copy, x+1, y+1):
                        spaces.append((x+1, y+1))
            if y > 0:
                if pieces[x+1][y-1] != ' ' and pieces[x+1][y-1].type != 'k' and pieces[x+1][y-1].team != 'b':
                    pieces_copy = setup.setup_copy_board(pieces)
                    pieces_copy = move(pieces_copy, pieces_copy[x][y], (x+1, y-1))
                    if not in_check(pieces_copy, x+1, y-1):
                        spaces.append((x+1, y-1))

    return spaces




# For moving through check, move one space at a time and check if it is in check
def check_king(pieces, x, y):

    spaces = []
    protected_list = []

    for row in pieces:
        for p in row:
            if p != ' ' and p.team != pieces[x][y].team:
                protected_list.append(protected_spaces(pieces, p, True))

    protected_list = list(chain.from_iterable(protected_list))
        
    for i in range(-1, 2):
        for j in range(-1, 2):
            if is_valid(x+i, y+j):
                if pieces[x+i][y+j] == ' ':
                    pieces_copy = setup.setup_copy_board(pieces)
                    pieces_copy = move(pieces_copy, pieces_copy[x][y], (x+i, y+j))
                    if not in_check(pieces_copy, x+i, y+j):
                        spaces.append((x+i, y+j))
                elif pieces[x+i][y+j].team != pieces[x][y].team and pieces[x+i][y+j].type != 'k':
                    pieces_copy = setup.setup_copy_board(pieces)
                    pieces_copy = move(pieces_copy, pieces_copy[x][y], (x+i, y+j))
                    if not in_check(pieces_copy, x+i, y+j):
                        spaces.append((x+i, y+j))

    intersection = set(spaces).intersection(protected_list)

    if len(intersection) > 0:
        for i in intersection:
            spaces.remove(i)

    
    if pieces[x][y].can_castle:
        if (x, y+1) in spaces:
            pieces_copy = setup.setup_copy_board(pieces)
            pieces_copy = move(pieces_copy, pieces_copy[x][y], (x, y+2))
            print(pieces_copy[x][7].can_castle)
            if not in_check(pieces_copy, x, y+2) and pieces_copy[x][7] != ' ' and pieces[x][7].can_castle:
                spaces.append((x, y+2))
        elif (x, y-1) in spaces:
            pieces_copy = setup.setup_copy_board(pieces)
            pieces_copy = move(pieces_copy, pieces_copy[x][y], (x, y-2))
            if not in_check(pieces_copy, x, y-2) and pieces_copy[x][0] != ' ' and pieces[x][0].can_castle:
                spaces.append((x, y-2))

                        
    return spaces




def check_rook(pieces, x, y, protected, check=False):

    spaces = []
    pieces_copy = pieces

    straights = [
        [[x + i, y] for i in range(1, 8)],
        [[x - i, y] for i in range(1, 8)],
        [[x, y + i] for i in range(1, 8)],
        [[x, y - i] for i in range(1, 8)]
    ]

    for row in straights:
        next_row = False
        for c in row:
            if is_valid(c[0], c[1]) and not next_row:
                if pieces[c[0]][c[1]] == ' ':
                    if not check:
                        pieces_copy = setup.setup_copy_board(pieces)
                        pieces_copy = move(pieces_copy, pieces_copy[x][y], (c[0], c[1]))
                        if not in_check(pieces_copy, c[0], c[1]):
                            spaces.append((c[0], c[1]))
                    else:
                        spaces.append((c[0], c[1]))
                elif not protected and pieces[x][y].team != pieces[c[0]][c[1]].team:
                    if not check:
                        pieces_copy = setup.setup_copy_board(pieces)
                        pieces_copy = move(pieces_copy, pieces_copy[x][y], (c[0], c[1]))
                        if not in_check(pieces_copy, c[0], c[1]):
                            spaces.append((c[0], c[1]))
                    else:
                        spaces.append((c[0], c[1]))
                    next_row = True
                elif protected and pieces[x][y].team == pieces[c[0]][c[1]].team and pieces[c[0]][c[1]].type != 'k':
                    spaces.append((c[0], c[1]))
                    next_row = True
                else:
                    next_row = True

    return spaces


def check_knight(pieces, x, y, protected, check=False):

    spaces = []

    for i in range(-2, 3):
        for j in range(-2, 3):
            if i**2 + j**2 == 5:
                if is_valid(x+i, y+j):
                    if pieces[x+i][y+j] == ' ': 
                        if not check:
                            pieces_copy = setup.setup_copy_board(pieces)
                            pieces_copy = move(pieces_copy, pieces_copy[x][y], (x+i,  y+j))
                            if not in_check(pieces_copy, x+i, y+j):
                                spaces.append((x+i, y+j))
                        else:
                            spaces.append((x+i, y+j))
                    elif not protected and pieces[x][y].team != pieces[x+i][y+j].team:
                        if not check:
                            pieces_copy = setup.setup_copy_board(pieces)
                            pieces_copy = move(pieces_copy, pieces_copy[x][y], (x+i,  y+j))
                            if not in_check(pieces_copy, x+i, y+j):
                                spaces.append((x+i, y+j))
                        else:
                            spaces.append((x+i, y+j))
                    elif protected and pieces[x][y].team == pieces[x+i][y+j].team and pieces[x+i][y+j].type != 'k':
                        spaces.append((x+i, y+j))
    return spaces


def check_queen(pieces, x, y, protected, check=False):

    spaces = []

    moves = [
        [[x + i, y + i] for i in range(1, 8)],
        [[x + i, y - i] for i in range(1, 8)],
        [[x - i, y + i] for i in range(1, 8)],
        [[x - i, y - i] for i in range(1, 8)],
        [[x + i, y] for i in range(1, 8)],
        [[x - i, y] for i in range(1, 8)],
        [[x, y + i] for i in range(1, 8)],
        [[x, y - i] for i in range(1, 8)]
    ]

    for row in moves:
        next_row = False
        for c in row:
            if is_valid(c[0], c[1]) and not next_row:
                if pieces[c[0]][c[1]] == ' ':
                    if not check:
                        pieces_copy = setup.setup_copy_board(pieces)
                        pieces_copy = move(pieces_copy, pieces_copy[x][y], (c[0], c[1]))
                        if not in_check(pieces_copy, c[0], c[1]):
                            spaces.append((c[0], c[1]))
                    else:
                        spaces.append((c[0], c[1]))
                elif not protected and pieces[x][y].team != pieces[c[0]][c[1]].team:
                    if not check:
                        pieces_copy = setup.setup_copy_board(pieces)
                        pieces_copy = move(pieces_copy, pieces_copy[x][y], (c[0], c[1]))
                        if not in_check(pieces_copy, c[0], c[1]):
                            spaces.append((c[0], c[1]))
                    else:
                        spaces.append((c[0], c[1]))
                    next_row = True
                elif protected and pieces[x][y].team == pieces[c[0]][c[1]].team and pieces[c[0]][c[1]].type != 'k':
                    spaces.append((c[0], c[1]))
                    next_row = True
                else:
                    next_row = True

    return spaces


def check_bishop(pieces, x, y, protected, check=False):

    spaces = []

    diagonals = [
        [[x + i, y + i] for i in range(1, 8)],
        [[x + i, y - i] for i in range(1, 8)],
        [[x - i, y + i] for i in range(1, 8)],
        [[x - i, y - i] for i in range(1, 8)]
    ]

    for row in diagonals:
        next_row = False
        for c in row:
            if is_valid(c[0], c[1]) and not next_row:
                if pieces[c[0]][c[1]] == ' ':
                    if not check:
                        pieces_copy = setup.setup_copy_board(pieces)
                        pieces_copy = move(pieces_copy, pieces_copy[x][y], (c[0], c[1]))
                        if not in_check(pieces_copy, c[0], c[1]):
                            spaces.append((c[0], c[1]))
                    else:
                        spaces.append((c[0], c[1]))
                elif not protected and pieces[x][y].team != pieces[c[0]][c[1]].team:
                    if not check:
                        pieces_copy = setup.setup_copy_board(pieces)
                        pieces_copy = move(pieces_copy, pieces_copy[x][y], (c[0], c[1]))
                        if not in_check(pieces_copy, c[0], c[1]):
                            spaces.append((c[0], c[1]))
                    else:
                        spaces.append((c[0], c[1]))
                    next_row = True
                elif protected and pieces[x][y].team == pieces[c[0]][c[1]].team and pieces[c[0]][c[1]].type != 'k':
                    spaces.append((c[0], c[1]))
                    next_row = True
                else:
                    next_row = True

    return spaces



###################
# Space checks
###################


def king_protected_spaces(pieces, x, y):

    spaces = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            if is_valid(x+i, y+j):
                if pieces[x+i][y+j] == ' ':
                    spaces.append((x+i, y+j))
                elif pieces[x+i][y+j].team == pieces[x][y].team:
                    spaces.append((x+i, y+j))

    return spaces


def pawn_protected_spaces(pieces, x, y):

    spaces = []

    for i in range(-1, 2, 2):
        for j in range(-1, 2, 2):
            if is_valid(x+i, y+j):
                if pieces[x+i][y+j] == ' ':
                    if pieces[x][y].team == 'b' and i > 0:
                        spaces.append((x+i, y+j))
                    elif pieces[x][y].team == 'w' and i < 0:
                        spaces.append((x+i, y+j))
                elif pieces[x+i][y+j].team != pieces[x][y].team:
                    if pieces[x][y].team == 'b' and i > 0:
                        spaces.append((x+i, y+j))
                    elif pieces[x][y].team == 'w' and i < 0:
                        spaces.append((x+i, y+j))

    return spaces


###################
# Helper functions 
###################

def is_valid(x, y):

    if x >= 0 and x <= 7:
        if y >= 0 and y <= 7:
            return True
    return False


def protected_spaces(pieces, p, protected, check=False):

    protected_list = []

    if p.type == 'p':
        a, b = conversions.pixels_to_list(p.pos[0], p.pos[1])
        protected_list.append(pawn_protected_spaces(pieces, a, b))
    elif p.type == 'r':
        a, b = conversions.pixels_to_list(p.pos[0], p.pos[1])
        protected_list.append(check_rook(pieces, a, b, protected, check))
    elif p.type == 'n':
        a, b = conversions.pixels_to_list(p.pos[0], p.pos[1])
        protected_list.append(check_knight(pieces, a, b, protected, check))
    elif p.type == 'b':
        a, b = conversions.pixels_to_list(p.pos[0], p.pos[1])
        protected_list.append(check_bishop(pieces, a, b, protected, check))
    elif p.type == 'q':
        a, b = conversions.pixels_to_list(p.pos[0], p.pos[1])
        protected_list.append(check_queen(pieces, a, b, protected, check))
    elif p.type == 'k':
        a, b = conversions.pixels_to_list(p.pos[0], p.pos[1])
        protected_list.append(king_protected_spaces(pieces, a, b))
    

     # might need to add in king check too, think through all that later
    
    return list(chain.from_iterable(protected_list))


def in_check(pieces, x, y):

    for row in pieces:
        for p in row:
            if p != ' ' and p.team == pieces[x][y].team and p.type == 'k':
                a, b = conversions.pixels_to_list(p.pos[0], p.pos[1])
                break

    for row in pieces:
        for p in row:
            if p != ' ' and p.team != pieces[x][y].team:
                for s in protected_spaces(pieces, p, False, True):
                    if s == (a, b):
                        return True
    
    return False


def move(pieces, piece, move):

    pieces[move[0]][move[1]] = piece
    p1, p2 = conversions.pixels_to_list(piece.pos[0], piece.pos[1])
    piece.pos = constant.POS_LIST[move[0]][move[1]]
    pieces[p1][p2] = ' '

    return pieces
