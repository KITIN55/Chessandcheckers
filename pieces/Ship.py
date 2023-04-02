from pieces.Piece import Piece


class Ship(Piece):
    def __init__(self, color, position):
        self.name = 'Ship'
        super(Ship, self).__init__(color, position)
        if self.color == 'w':
            self.image = 'images/white_ship.png'
        else:
            self.image = 'images/black_ship.png'

        self.value = 7

    def get_possible_moves(self, board):
        possible_moves = []

        current_row, current_col = self.position

        for i in range(current_row+1, 8):
            if board[i][current_col] is None:
                possible_moves.append((i, current_col))
            elif board[i][current_col].color != self.color:
                possible_moves.append((i, current_col))
                break
            else:
                break

        for i in range(current_row-1, -1, -1):
            if board[i][current_col] is None:
                possible_moves.append((i, current_col))
            elif board[i][current_col].color != self.color:
                possible_moves.append((i, current_col))
                break
            else:
                break

        for j in range(current_col+1, 8):
            if board[current_row][j] is None:
                possible_moves.append((current_row, j))
            elif board[current_row][j].color != self.color:
                possible_moves.append((current_row, j))
                break
            else:
                break

        for j in range(current_col-1, -1, -1):
            if board[current_row][j] is None:
                possible_moves.append((current_row, j))
            elif board[current_row][j].color != self.color:
                possible_moves.append((current_row, j))
                break
