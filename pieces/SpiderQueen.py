from pieces.Piece import Piece


class SpiderQueen(Piece):
    def __init__(self, color, position):
        self.name = 'SpiderQueen'
        super(SpiderQueen, self).__init__(color, position)
        if self.color == 'w':
            self.image = 'images/white_spiderqueen.png'
        else:
            self.image = 'images/black_spiderqueen.png'

        self.value = 9

    def get_possible_moves(self, board):
        moves = []
        for d in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
            for i in range(1, 4):
                next_pos = (self.position[0] + i * d[0], self.position[1] + i * d[1])
                if not board.is_on_board(next_pos):
                    break
                piece_at_pos = board.get_piece_at_position(next_pos)
                if piece_at_pos is None:
                    moves.append(next_pos)
                else:
                    if piece_at_pos.color != self.color:
                        moves.append(next_pos)
                    break

        moves += self.get_possible_straight_line_moves(board)
        moves += self.get_possible_diagonal_line_moves(board)
        return moves