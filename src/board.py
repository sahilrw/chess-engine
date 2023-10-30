from const import *
from square import Square
from piece import *
from move import Move


class Board:
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
        self._create()
        self._add_pieces("white")
        self._add_pieces("black")

    def calc_moves(self, piece, row, col):
        def knight_moves():
            # 8 possible moves for knight(L direction)
            possible_moves = [
                (row - 1, col + 2),
                (row + 1, col + 2),
                (row - 2, col + 1),
                (row + 1, col - 2),
                (row - 2, col - 1),
                (row + 2, col - 1),
                (row - 1, col - 2),
                (row + 2, col + 1),
            ]

            # loop to check whether any of the moves is valid
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move

                # check whether the move is in range(on board == square 0 to 7)
                if Square.in_range(possible_move_row, possible_move_col):
                    # check whether square is empty or it has opponent piece
                    if self.squares[possible_move_row][
                        possible_move_col
                    ].isempty_or_rival(piece.color):
                        # if the condition satisfy then it is a valid move
                        # create squares of new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        # create new move
                        move = Move(initial, final)
                        piece.add_move(move)

        if piece.name == "Pawn":
            pass

        elif isinstance(piece, Knight):
            knight_moves()

        elif piece.name == "Bishop":
            pass

        elif piece.name == "Rook":
            pass

        elif piece.name == "Queen":
            pass

        elif piece.name == "King":
            pass

    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        row_pawn, row_other = (6, 7) if color == "white" else (1, 0)

        # pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        # knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        # bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

        # rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        # queens
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))

        # king
        self.squares[row_other][4] = Square(row_other, 4, King(color))
