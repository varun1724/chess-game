import piece
import constant



def setup_board() -> list:

        board = [[' ' for _ in range(0, 8)] for _ in range(0, 8)]

        board[0] = [
            piece.Piece('b', 'r', constant.PIECE_IMGS[0], constant.POS_LIST[0][0]),
            piece.Piece('b', 'n', constant.PIECE_IMGS[1], constant.POS_LIST[0][1]),
            piece.Piece('b', 'b', constant.PIECE_IMGS[2], constant.POS_LIST[0][2]),
            piece.Piece('b', 'q', constant.PIECE_IMGS[3], constant.POS_LIST[0][3]),
            piece.Piece('b', 'k', constant.PIECE_IMGS[4], constant.POS_LIST[0][4]),
            piece.Piece('b', 'b', constant.PIECE_IMGS[2], constant.POS_LIST[0][5]),
            piece.Piece('b', 'n', constant.PIECE_IMGS[1], constant.POS_LIST[0][6]),
            piece.Piece('b', 'r', constant.PIECE_IMGS[0], constant.POS_LIST[0][7])
        ]

        board[7] = [
            piece.Piece('w', 'r', constant.PIECE_IMGS[7], constant.POS_LIST[7][0]),
            piece.Piece('w', 'n', constant.PIECE_IMGS[8], constant.POS_LIST[7][1]),
            piece.Piece('w', 'b', constant.PIECE_IMGS[9], constant.POS_LIST[7][2]),
            piece.Piece('w', 'q', constant.PIECE_IMGS[10], constant.POS_LIST[7][3]),
            piece.Piece('w', 'k', constant.PIECE_IMGS[11], constant.POS_LIST[7][4]),
            piece.Piece('w', 'b', constant.PIECE_IMGS[9], constant.POS_LIST[7][5]),
            piece.Piece('w', 'n', constant.PIECE_IMGS[8], constant.POS_LIST[7][6]),
            piece.Piece('w', 'r', constant.PIECE_IMGS[7], constant.POS_LIST[7][7])
        ]

        for i in range(0, 8):
            board[1][i] = piece.Piece('b', 'p', constant.PIECE_IMGS[5], constant.POS_LIST[1][i])
            board[6][i] = piece.Piece('w', 'p', constant.PIECE_IMGS[6], constant.POS_LIST[6][i])


        return board


def setup_graphics() -> dict:

    graphics = {
        (0, 0): constant.PIECE_IMGS[0], (1, 0): constant.PIECE_IMGS[1], (2, 0): constant.PIECE_IMGS[2], (3, 0): constant.PIECE_IMGS[3],
        (4, 0): constant.PIECE_IMGS[4], (5, 0): constant.PIECE_IMGS[2], (6, 0): constant.PIECE_IMGS[1], (7, 0): constant.PIECE_IMGS[0],

        (0, 1): constant.PIECE_IMGS[5], (1, 1): constant.PIECE_IMGS[5], (2, 1): constant.PIECE_IMGS[5], (3, 1): constant.PIECE_IMGS[5],
        (4, 1): constant.PIECE_IMGS[5], (5, 1): constant.PIECE_IMGS[5], (6, 1): constant.PIECE_IMGS[5], (7, 1): constant.PIECE_IMGS[5],

        (0, 2): None, (1, 2): None, (2, 2): None, (3, 2): None,
        (4, 2): None, (5, 2): None, (6, 2): None, (7, 2): None,

        (0, 3): None, (1, 3): None, (2, 3): None, (3, 3): None,
        (4, 3): None, (5, 3): None, (6, 3): None, (7, 3): None,

        (0, 4): None, (1, 4): None, (2, 4): None, (3, 4): None,
        (4, 4): None, (5, 4): None, (6, 4): None, (7, 4): None,

        (0, 5): None, (1, 5): None, (2, 5): None, (3, 5): None,
        (4, 5): None, (5, 5): None, (6, 5): None, (7, 5): None,

        (0, 6): constant.PIECE_IMGS[6], (1, 6): constant.PIECE_IMGS[6], (2, 6): constant.PIECE_IMGS[6], (3, 6): constant.PIECE_IMGS[5],
        (4, 6): constant.PIECE_IMGS[6], (5, 6): constant.PIECE_IMGS[6], (6, 6): constant.PIECE_IMGS[6], (7, 6): constant.PIECE_IMGS[6],

        (0, 7): constant.PIECE_IMGS[7], (1, 7): constant.PIECE_IMGS[8], (2, 7): constant.PIECE_IMGS[9], (3, 7): constant.PIECE_IMGS[10],
        (4, 7): constant.PIECE_IMGS[11], (5, 7): constant.PIECE_IMGS[9], (6, 7): constant.PIECE_IMGS[8], (7, 7): constant.PIECE_IMGS[7]
    }

    return graphics