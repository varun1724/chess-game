import constant
import conversions

# Returns a list of x, y coords
def check_moves(pieces, x_coord, y_coord):

    x, y = conversions.pixels_to_list(x_coord, y_coord)
    
    if pieces[x][y].type == 'p':
        return check_pawn(pieces, x, y)
    elif pieces[x][y].type == 'r':
        return check_rook(pieces, x, y)
    elif pieces[x][y].type == 'n':
        return check_knight(pieces, x, y)
    elif pieces[x][y].type == 'b':
        return check_bishop(pieces, x, y)
    elif pieces[x][y].type == 'q':
        return check_queen(pieces, x, y)
    else:
        return check_king(pieces, x, y)


# Still need to code promotion and en pasant 
def check_pawn(pieces, x, y):

    spaces = []

    if pieces[x][y].team == 'w':
        if x > 0:
            if pieces[x-1][y] == ' ':
                spaces.append((x-1, y))
            if x == 6 and pieces[x-2][y] == ' ':
                spaces.append((x-2, y))
            if y < 7:
                if pieces[x-1][y+1] != ' ' and pieces[x-1][y+1].type != 'k' and pieces[x-1][y+1].team != 'w':
                    spaces.append((x-1, y+1))
            if y > 0:
                if pieces[x-1][y-1] != ' ' and pieces[x-1][y-1].type != 'k' and pieces[x-1][y-1].team != 'w':
                    spaces.append((x-1, y-1))
    else:
        if x < 7:
            if pieces[x+1][y] == ' ':
                spaces.append((x+1, y))
            if x == 1 and pieces[x+2][y] == ' ':
                spaces.append((x+2, y))
            if y < 7:
                if pieces[x+1][y+1] != ' ' and pieces[x+1][y+1].type != 'k' and pieces[x+1][y+1].team != 'b':
                    spaces.append((x+1, y+1))
            if y > 0:
                if pieces[x+1][y-1] != ' ' and pieces[x+1][y-1].type != 'k' and pieces[x+1][y-1].team != 'b':
                    spaces.append((x+1, y-1))

    return spaces


def check_king(pieces, x, y):

    if pieces[x][y].team == 'w':
        pass

    else:
        pass

    return "king"

def check_rook(pieces, x, y):

    spaces = []

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
                    spaces.append((c[0], c[1]))
                elif pieces[x][y].team != pieces[c[0]][c[1]].team and pieces[c[0]][c[1]].type != 'k':
                    spaces.append((c[0], c[1]))
                    next_row = True
                else:
                    next_row = True

    return spaces


def check_knight(pieces, x, y):

    spaces = []

    for i in range(-2, 3):
        for j in range(-2, 3):
            if i**2 + j**2 == 5:
                if is_valid(x+i, y+j):
                    if pieces[x+i][y+j] == ' ': 
                        spaces.append((x+i, y+j))
                    elif pieces[x][y].team != pieces[x+i][y+j].team and pieces[x+i][y+j].type != 'k':
                        spaces.append((x+i, y+j))
    return spaces


def check_queen(pieces, x, y):

    spaces = []

    if pieces[x][y].team == 'w':
        pass

    else:
        pass 

    return spaces


def check_bishop(pieces, x, y):

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
                    spaces.append((c[0], c[1]))
                elif pieces[x][y].team != pieces[c[0]][c[1]].team and pieces[c[0]][c[1]].type != 'k':
                    spaces.append((c[0], c[1]))
                    next_row = True
                else:
                    next_row = True

    return spaces



def is_valid(x, y):

    if x >= 0 and x <= 7:
        if y >= 0 and y <= 7:
            return True
    return False



