import pygame
from PIL import ImageColor

class Background:

    base = ImageColor.getcolor("#f8e7bb", "RGB")
    layer = ImageColor.getcolor("#964d22", "RGB")

    def __init__(self, width, height):
        self.width = width / 8
        self.height = height / 8


    def draw(self, win):

        win.fill(self.base)

        for i in range(1, 9, 2):
            for j in range(0, 8):
                if j % 2 == 1:
                    pygame.draw.rect(win, self.layer, (i*self.width, j*self.height, self.width, self.height))
                else:
                    pygame.draw.rect(win, self.layer, ((i-1)*self.width, j*self.height, self.width, self.height))




