import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE, HEIGHT_BELT, FONT, BLACK, GREY
from checkers.game import Game
from checkers.Exceptions import OutsideBoardExceptions


FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT_BELT))
pygame.display.set_caption("checkers")


def get_row_col_from_mouse(pos):

    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():

    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                print(row, col)
                try:
                    game.select(row, col)
                except OutsideBoardExceptions:
                    game.outside_board_exce = True
                    print("outside board exce")
        pygame.display.update()

        game.update()


    pygame.quit()



main()
