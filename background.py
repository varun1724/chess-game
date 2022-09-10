import pygame
import constant
import conversions
from PIL import ImageColor


class Background:

    base_color = ImageColor.getcolor("#f8e7bb", "RGB")
    layer_color = ImageColor.getcolor("#964d22", "RGB")
    selected_color = (129, 207, 106)
    move_option_color = (169, 169, 169)

    def __init__(self, width, height, x=-1, y=-1, move_list=[], selected=False, can_move=False):
        self.width = width / 8
        self.height = height / 8
        self.x = x
        self.y = y
        self.move_list = move_list
        self.selected = selected
        self.can_move = can_move

    def draw(self, win):

        win.fill(self.base_color)

        for i in range(1, 9, 2):
            for j in range(0, 8):
                if j % 2 == 1:
                    pygame.draw.rect(win, self.layer_color, (i*self.width, j*self.height, self.width, self.height))
                else:
                    pygame.draw.rect(win, self.layer_color, ((i-1)*self.width, j*self.height, self.width, self.height))

        if self.selected:
            pygame.draw.rect(win, self.selected_color, (self.x, self.y, self.width, self.height))

            if self.can_move:
                for s in self.move_list:
                    # print(constant.POS_LIST[s[0]][s[1]][0])
                    pygame.draw.rect(win, self.move_option_color, (constant.POS_LIST[s[0]][s[1]][0], constant.POS_LIST[s[0]][s[1]][1], self.width, self.height))


    def move(self, pieces, piece, move):

        pieces[move[0]][move[1]] = piece
        p1, p2 = conversions.pixels_to_list(piece.pos[0], piece.pos[1])
        piece.pos = constant.POS_LIST[move[0]][move[1]]
        pieces[p1][p2] = ' '

        return pieces


