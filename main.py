import constant
import background
import pygame
import draw_game


def main():

    bg = background.Background(constant.WIN_WIDTH, constant.WIN_HEIGHT)

    win = pygame.display.set_mode((constant.WIN_WIDTH, constant.WIN_HEIGHT))
    clock = pygame.time.Clock()

    run = True

    while run:

        clock.tick(20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False




        draw_game.draw_window(win, bg)

    
    pygame.quit()
    quit()

main()