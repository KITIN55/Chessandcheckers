import pygame

# inicjalizacja modułu czcionek, określenie rozmiarów kwadratu dla naszej szachownicy, liczba pól
pygame.font.init()
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
BELT = WIDTH // 8
HEIGHT_BELT = HEIGHT + BELT
# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
GREEN = (0, 150, 0)
GOLD = (200, 180, 0)


CROWN = pygame.transform.scale(pygame.image.load('checkers/crown.png'), (WIDTH // 20, HEIGHT // 38))
FONT = pygame.font.Font('checkers/arial.ttf', 20)
FONT2 = pygame.font.Font('checkers/arial.ttf', 40)
