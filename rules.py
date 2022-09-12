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

# white rook not capturing pond until the other rook moves
def check_rook(pieces, x, y):

    spaces = []

    if pieces[x][y].team == 'w':
        if x < 7:
            i = x + 1
            while i < 8:
                if pieces[i][y] == ' ': 
                    spaces.append((i, y))
                elif pieces[i][y].team == 'b' and pieces[i][y].type != 'k':
                    spaces.append((i, y))
                    break
                else:
                    break
                i += 1
        if x > 0:
            i = x - 1
            while i > -1:
                if pieces[i][y] == ' ': 
                    spaces.append((i, y))
                elif pieces[i][y].team == 'b' and pieces[i][y].type != 'k':
                    spaces.append((i, y))
                    break
                else:
                    break
                i -= 1
        if y < 7:
            i = y + 1
            while i < 8:
                if pieces[x][i] == ' ': 
                    spaces.append((x, i))
                elif pieces[x][i].team == 'b' and pieces[x][i].type != 'k':
                    spaces.append((x, i))
                    break
                else:
                    break
                i += 1
        if y > 0:
            i = y - 1
            while i > -1:
                if pieces[x][i] == ' ': 
                    spaces.append((x, i))
                elif pieces[x][i].team == 'b' and pieces[x][i].type != 'k':
                    spaces.append((x, i))
                    break
                else:
                    break
                i -= 1
    else:
        if x < 7:
            i = x + 1
            while i < 8:
                if pieces[i][y] == ' ': 
                    spaces.append((i, y))
                elif pieces[i][y].team == 'w' and pieces[i][y].type != 'k':
                    spaces.append((i, y))
                    break
                else:
                    break 
                i += 1
        if x > 0:
            i = x - 1
            while i > -1:
                if pieces[i][y] == ' ':  
                    spaces.append((i, y))
                elif pieces[i][y].team == 'w' and pieces[i][y].type != 'k':
                    spaces.append((i, y))
                    break
                i -= 1
        if y < 7:
            i = y + 1
            while i < 8:
                if pieces[x][i] == ' ':  
                    spaces.append((x, i))
                elif pieces[x][i].team == 'w' and pieces[x][i].type != 'k':
                    spaces.append((x, i))
                    break
                i += 1
        if y > 0:
            i = y - 1
            while i > -1:
                if pieces[x][i] == ' ':  
                    spaces.append((x, i))
                elif pieces[x][i].team == 'w' and pieces[x][i].type != 'k':
                    spaces.append((x, i))
                    break
                i -= 1
        

    return spaces


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







