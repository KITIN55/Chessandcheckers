import pygame
from pygame.locals import *
import time
from pieces.Queen import Queen

from ChessBoard import ChessBoard


class Game:
    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode((900, 650))
        pygame.display.set_caption('Chess')

        self.settings = {'board_image': 'images/orange_board.png'}
        self.board_image = pygame.image.load(self.settings['board_image'])

        self.clock = pygame.time.Clock()
        self.chess_board = ChessBoard()

        self.curr_selected_piece = None
        self.curr_poss_moves = []
        self.all_poss_moves = self.get_all_poss_moves()

        self.white_pieces_taken_images = []
        self.black_pieces_taken_images = []

        self.play_game()

    def play_game(self):

        while True:

            # Draw whole window (and draw board)
            self.draw_window()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                if event.type == pygame.MOUSEBUTTONUP:
                    # Get user click
                    self.get_user_click()

            # pygame.display.flip()
            self.clock.tick(60)

    def draw_window(self):

        self.game_display.fill(white)

        self.draw_side_menu()

        self.draw_board()
        pygame.display.update()

    def draw_side_menu(self):

        pygame.draw.rect(self.game_display, black, Rect((650, 100), (200, 400)), 5)


        if self.chess_board.curr_player == 'b':
            pygame.draw.rect(self.game_display, blue, Rect((700, 25), (100, 50)), 5)
        else:
            pygame.draw.rect(self.game_display, blue, Rect((700, 525), (100, 50)), 5)

        self.message_display('Black', (750, 50), fontsize=30)
        self.message_display('White', (750, 550), fontsize=30)


        start = 0
        if len(self.get_all_played_moves()) > 10:
            start = len(self.get_all_played_moves()) - 10
        for i, move in enumerate(self.get_all_played_moves()[start:]):
            self.message_display(move, (740, 125 + (i * 30)), fontsize=20)
            start += 1


        for i, image in enumerate(self.black_pieces_taken_images):
            image = pygame.image.load(image)
            image = pygame.transform.scale(image, (30, 30))
            pos = 610 + i * 20, 5
            self.game_display.blit(image, pos)


        for i, image in enumerate(self.white_pieces_taken_images):
            image = pygame.image.load(image)
            image = pygame.transform.scale(image, (30, 30))
            pos = 610 + i * 20, 595
            self.game_display.blit(image, pos)

    def draw_board(self):

        self.game_display.blit(self.board_image, (0, 0))


        for piece in self.chess_board.get_all_pieces():
            image_position = piece.position
            image_position = image_position[0] * 75, (7 - image_position[1]) * 75
            piece_image = pygame.image.load(piece.image)
            self.game_display.blit(piece_image, image_position)


        if self.curr_selected_piece:

            box_x, box_y = self.convert_space_to_coordinates(self.curr_selected_piece.position)
            pygame.draw.rect(self.game_display, blue, Rect((box_x, box_y), (75, 75)), 5)

            for move in self.curr_poss_moves:
                box1_x, box1_y = self.convert_space_to_coordinates(move)
                pygame.draw.rect(self.game_display, red, Rect((box1_x, box1_y), (75, 75)), 5)

    def get_user_click(self):

        x, y = pygame.mouse.get_pos()

        if y > 600:
            pass

        elif x > 600:
            pass

        else:

            selected_space = self.convert_coordinates_to_space(x, y)

            if not self.curr_selected_piece:


                if self.is_piece_of_curr_player(selected_space):
                    self.new_piece_selected(selected_space)


            else:

                if selected_space == self.curr_selected_piece.position:
                    self.deselect_piece()


                elif selected_space in self.curr_poss_moves:

                    if self.curr_selected_piece.name == 'King' and selected_space in self.chess_board.get_castle_moves_for_curr_player():

                            self.add_move(self.curr_selected_piece.position, selected_space)
                            self.chess_board.castle_king(self.curr_selected_piece, selected_space)

                    else:

                        self.add_move(self.curr_selected_piece.position, selected_space)
                        self.move_piece(self.curr_selected_piece, selected_space)

                        if self.curr_selected_piece.name == 'Pawn' and selected_space[1] == 0 or selected_space[1] == 7:
                            self.chess_board.board[selected_space[0]][selected_space[1]] = None
                            self.chess_board.board[selected_space[0]][selected_space[1]] = Queen(self.chess_board.curr_player, selected_space)


                    self.deselect_piece()

                    self.change_curr_player()


                    self.all_poss_moves = self.get_all_poss_moves()
                    checkmate = True
                    for piece_pos in self.all_poss_moves:
                        if len(self.all_poss_moves[piece_pos]) != 0:
                            checkmate = False
                    if checkmate:
                        self.draw_window()
                        self.message_display('Checkmate!', (400, 300))
                        winner = 'White' if self.chess_board.curr_player == 'b' else 'Black'
                        self.message_display('%s wins!' % winner, (400, 400))
                        pygame.display.update()
                        time.sleep(2)
                        quit()


                elif selected_space in [piece.position for piece in self.chess_board.get_curr_player_pieces()]:

                    self.new_piece_selected(selected_space)


                else:

                    self.deselect_piece()

    def convert_coordinates_to_space(self, x, y):

        return x // 75, 7 - y // 75

    def convert_space_to_coordinates(self, position):

        return position[0] * 75, (7 - position[1]) * 75

    def is_piece_of_curr_player(self, space):

        for piece in self.chess_board.get_curr_player_pieces():
            if space == piece.position:
                return True

    def get_all_poss_moves(self):

        moves = {}
        pieces = self.chess_board.get_curr_player_pieces()
        for piece in pieces:
            p_moves = self.chess_board.get_poss_moves_for(piece)
            moves[piece.position] = self.chess_board.is_curr_player_in_check(piece, p_moves)
        return moves

    def get_curr_poss_moves(self):

        return self.all_poss_moves[self.curr_selected_piece.position]

    def get_all_played_moves(self):
        return self.chess_board.played_moves

    def move_piece(self, piece, new_position):

        piece_captured = self.chess_board.move_piece(piece, new_position)
        if piece_captured:
            self.piece_was_captured(piece_captured)

    def change_curr_player(self):

        self.chess_board.curr_player = 'w' if self.chess_board.curr_player == 'b' else 'b'

    def new_piece_selected(self, new_space):

        self.curr_selected_piece = self.chess_board.get_piece_at(new_space)
        self.curr_poss_moves = self.get_curr_poss_moves()

    def deselect_piece(self):

        self.curr_selected_piece = None
        self.curr_poss_moves = None

    def add_move(self, pos_1, pos_2):

        name = self.chess_board.curr_player.upper() + ':     '
        move = name + self.convert_coordinate_to_space_name(pos_1) + ' -> ' + self.convert_coordinate_to_space_name(pos_2)
        self.chess_board.played_moves.append(move)

    def convert_coordinate_to_space_name(self, coordinate):

        conversions = {0 : 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}
        return str(conversions[coordinate[0]]) + str(coordinate[1] + 1)

    def piece_was_captured(self, piece):

        if piece.color == 'w':
            self.white_pieces_taken_images.append(piece.image)
        else:
            self.black_pieces_taken_images.append(piece.image)

    def message_display(self, text, point, fontsize=90):

        large_text = pygame.font.Font('freesansbold.ttf', fontsize)
        text_surface = large_text.render(text, True, black)
        text_rect = text_surface.get_rect()
        text_rect.center = (point)
        self.game_display.blit(text_surface, text_rect)

if __name__ == '__main__':

    white = (255,255,255)
    blue = (34, 0, 255)
    red = (209, 9, 9)
    black = (0, 0, 0)
    Game()
