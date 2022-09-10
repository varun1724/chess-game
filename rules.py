import constant
import conversions

# Returns a list of x, y coords
def check_moves(pieces, x_coord, y_coord):

    x, y = conversions.pixels_to_list(x_coord, y_coord)

    # print(pieces[x][y])
    
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


def check_pawn(pieces, x, y):

    spaces = []

    if pieces[x][y].team == 'w':
        if pieces[x-1][y] == ' ':
            spaces.append((x-1, y))
        if x == 6 and pieces[x-2][y] == ' ':
            spaces.append((x-2, y))
        if y > 0 and y < 7:
            if pieces[x-1][y+1] != ' ' and pieces[x-1][y+1].type != 'k' and pieces[x-1][y+1].team != 'b':
                spaces.append((x-1, y+1))
            if pieces[x-1][y-1] != ' ' and pieces[x-1][y-1].type != 'k' and pieces[x-1][y-1].team != 'b':
                spaces.append((x-1, y-1))

    else:
        pass

    return spaces


def check_king(pieces, x, y):

    if pieces[x][y].team == 'w':
        pass

    else:
        pass

    return "king"


def check_rook(pieces, x, y):

    if pieces[x][y].team == 'w':
        pass

    else:
        pass

    return "rook"


def check_knight(pieces, x, y):

    if pieces[x][y].team == 'w':
        pass

    else:
        pass

    return "knight"


def check_queen(pieces, x, y):

    if pieces[x][y].team == 'w':
        pass

    else:
        pass

    return "queen"


def check_bishop(pieces, x, y):

    if pieces[x][y].team == 'w':
        pass

    else:
        pass

    return "bishop"







