import pygame
import constant
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

    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.y = y

    def set_selected(self, selected):
        self.selected = selected

    def set_move_state(self, can_move):
        self.can_move = can_move

    def set_move_list(self, move_list):
        self.move_list = move_list


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

        




