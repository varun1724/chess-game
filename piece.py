import constant

class Piece:

    def __init__(self, team, type, image, pos, can_kill=False):
        self.team = team
        self.type = type
        self.img = image
        self.pos = pos
        self.can_kill = can_kill


    def set_pos(self, pos):
        self.pos = pos


    def draw(self, win):

        win.blit(self.img, self.pos)
