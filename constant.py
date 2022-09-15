import pygame
import os

WIN_HEIGHT = 820
WIN_WIDTH = 800


PIECE_IMGS = [
    pygame.transform.scale(pygame.image.load(os.path.join("chess-imgs", "Chess_rdt60.png")), (100, 100)),
    pygame.transform.scale(pygame.image.load(os.path.join("chess-imgs", "Chess_ndt60.png")), (100, 100)),
    pygame.transform.scale(pygame.image.load(os.path.join("chess-imgs", "Chess_bdt60.png")), (100, 100)),
    pygame.transform.scale(pygame.image.load(os.path.join("chess-imgs", "Chess_qdt60.png")), (100, 100)),
    pygame.transform.scale(pygame.image.load(os.path.join("chess-imgs", "Chess_kdt60.png")), (100, 100)),
    pygame.transform.scale(pygame.image.load(os.path.join("chess-imgs", "Chess_pdt60.png")), (100, 100)),
    pygame.transform.scale(pygame.image.load(os.path.join("chess-imgs", "Chess_plt60.png")), (100, 100)),
    pygame.transform.scale(pygame.image.load(os.path.join("chess-imgs", "Chess_rlt60.png")), (100, 100)),
    pygame.transform.scale(pygame.image.load(os.path.join("chess-imgs", "Chess_nlt60.png")), (100, 100)),
    pygame.transform.scale(pygame.image.load(os.path.join("chess-imgs", "Chess_blt60.png")), (100, 100)),
    pygame.transform.scale(pygame.image.load(os.path.join("chess-imgs", "Chess_qlt60.png")), (100, 100)),
    pygame.transform.scale(pygame.image.load(os.path.join("chess-imgs", "Chess_klt60.png")), (100, 100)),
]


POS_LIST = [
    [(0, 0), (100, 0), (200, 0), (300, 0), (400, 0), (500, 0), (600, 0), (700, 0)],
    [(0, 100), (100, 100), (200, 100), (300, 100), (400, 100), (500, 100), (600, 100), (700, 100)],
    [(0, 200), (100, 200), (200, 200), (300, 200), (400, 200), (500, 200), (600, 200), (700, 200)],
    [(0, 300), (100, 300), (200, 300), (300, 300), (400, 300), (500, 300), (600, 300), (700, 300)],
    [(0, 400), (100, 400), (200, 400), (300, 400), (400, 400), (500, 400), (600, 400), (700, 400)],
    [(0, 500), (100, 500), (200, 500), (300, 500), (400, 500), (500, 500), (600, 500), (700, 500)],
    [(0, 600), (100, 600), (200, 600), (300, 600), (400, 600), (500, 600), (600, 600), (700, 600)],
    [(0, 700), (100, 700), (200, 700), (300, 700), (400, 700), (500, 700), (600, 700), (700, 700)],
]