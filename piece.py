import constant
import pygame

class Piece:

    def __init__(self, team, type, image, pos, can_kill=False):
        self.team = team
        self.type = type
        self.img = image
        self.pos = pos
        self.can_kill = can_kill


    def draw(self, win):

        win.blit(self.img, self.pos)



    def get_mask_rect(self):

        rect = pygame.mask.from_surface(self.img).get_rect()

        rect.x = self.pos[0]
        rect.y = self.pos[1]

        return rect
