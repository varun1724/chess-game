import piece
import constant


def setup_board() -> list:

        board = [[' ' for _ in range(0, 8)] for _ in range(0, 8)]

        board[0] = [
            piece.Piece('b', 'r', constant.PIECE_IMGS[0], constant.POS_LIST[0][0], can_castle=True),
            piece.Piece('b', 'n', constant.PIECE_IMGS[1], constant.POS_LIST[0][1]),
            piece.Piece('b', 'b', constant.PIECE_IMGS[2], constant.POS_LIST[0][2]),
            piece.Piece('b', 'q', constant.PIECE_IMGS[3], constant.POS_LIST[0][3]),
            piece.Piece('b', 'k', constant.PIECE_IMGS[4], constant.POS_LIST[0][4], can_castle=True),
            piece.Piece('b', 'b', constant.PIECE_IMGS[2], constant.POS_LIST[0][5]),
            piece.Piece('b', 'n', constant.PIECE_IMGS[1], constant.POS_LIST[0][6]),
            piece.Piece('b', 'r', constant.PIECE_IMGS[0], constant.POS_LIST[0][7], can_castle=True)
        ]

        board[7] = [
            piece.Piece('w', 'r', constant.PIECE_IMGS[7], constant.POS_LIST[7][0], can_castle=True),
            piece.Piece('w', 'n', constant.PIECE_IMGS[8], constant.POS_LIST[7][1]),
            piece.Piece('w', 'b', constant.PIECE_IMGS[9], constant.POS_LIST[7][2]),
            piece.Piece('w', 'q', constant.PIECE_IMGS[10], constant.POS_LIST[7][3]),
            piece.Piece('w', 'k', constant.PIECE_IMGS[11], constant.POS_LIST[7][4], can_castle=True),
            piece.Piece('w', 'b', constant.PIECE_IMGS[9], constant.POS_LIST[7][5]),
            piece.Piece('w', 'n', constant.PIECE_IMGS[8], constant.POS_LIST[7][6]),
            piece.Piece('w', 'r', constant.PIECE_IMGS[7], constant.POS_LIST[7][7], can_castle=True)
        ]

        for i in range(0, 8):
            board[1][i] = piece.Piece('b', 'p', constant.PIECE_IMGS[5], constant.POS_LIST[1][i])
            board[6][i] = piece.Piece('w', 'p', constant.PIECE_IMGS[6], constant.POS_LIST[6][i])


        return board

def setup_copy_board(pieces):

    board = setup_board()

    for x, row in enumerate(pieces):
        for y, p in enumerate(row):
            if p == ' ':
                board[x][y] = ' '
            else:
                board[x][y] = piece.Piece(p.team, p.type, p.img, p.pos)
    
    return board