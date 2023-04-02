from pieces.Piece import Piece


class KnightPawn(Piece):
    def __init__(self, color, position):
        self.name = 'Knight Pawn'
        super(KnightPawn, self).__init__(color, position)
        if self.color == 'w':
            self.image = 'images/white_kpawn.png'
        else:
            self.image = 'images/black_kpawn.png'

        self.value = 1

    def get_possible_moves(self, board):
        possible_moves = []

        current_row, current_col = self.position

        if self.color == 'w':
            if current_row > 1:
                if current_col > 0:
                    possible_moves.append((current_row-2, current_col-1))
                if current_col < 7:
                    possible_moves.append((current_row-2, current_col+1))

        else:
            if current_row < 6:
                if current_col > 0:
                    possible_moves.append((current_row+2, current_col-1))
                if current_col < 7:
                    possible_moves.append((current_row+2, current_col+1))

        return self.filter_moves_on_board(possible_moves, board)