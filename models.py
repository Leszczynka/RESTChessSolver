from abc import ABC, abstractmethod

BOARD = [[letter+number for letter in 'ABCDEFGH'] for number in '12345678']


class Figure(ABC):
    def __init__(self, position: str):
        self.position = position
        self.row_index, self.col_index = self.get_index_from_the_board()

    @abstractmethod
    def list_available_moves(self) -> list[str]:
        pass

    def validate_move(self, dest_field: str) -> bool:
        return dest_field in self.list_available_moves()

    def get_index_from_the_board(self):
        row_index = [BOARD.index(row) for row in BOARD if self.position in row][0]
        col_index = [row.index(self.position) for row in BOARD if self.position in row][0]
        return row_index, col_index

    def get_vertical_and_horizontal_moves(self):
        moves = []
        for x in range(len(BOARD)):
            if BOARD[self.row_index][x] != self.position:
                moves.append(BOARD[self.row_index][x])
            if BOARD[x][self.col_index] != self.position:
                moves.append(BOARD[x][self.col_index])
        return moves

    def get_diagonal_moves(self):
        moves = []
        for x in range(len(BOARD)):
            for y in range(len(BOARD)):
                if abs(self.row_index-x) == abs(self.col_index-y) and BOARD[x][y] != self.position:
                    moves.append(BOARD[x][y])
        return moves


class King(Figure):
    def list_available_moves(self) -> list[str]:
        available_moves = []
        for x in range(self.row_index-1, self.row_index+2):
            for y in range(self.col_index-1, self.col_index+2):
                if 0 <= x <= 7 and 0 <= y <= 7 and BOARD[x][y] != self.position:
                    available_moves.append(BOARD[x][y])
        return available_moves


class Queen(Figure):
    def list_available_moves(self) -> list[str]:
        available_moves = self.get_vertical_and_horizontal_moves() + self.get_diagonal_moves()
        return available_moves


class Rook(Figure):
    def list_available_moves(self) -> list[str]:
        return self.get_vertical_and_horizontal_moves()


class Bishop(Figure):
    def list_available_moves(self) -> list[str]:
        return self.get_diagonal_moves()


class Knight(Figure):
    def list_available_moves(self) -> list[str]:
        available_moves = []
        unavailable_moves = self.get_diagonal_moves() + self.get_vertical_and_horizontal_moves()
        for x in range(self.row_index-2, self.row_index+3):
            for y in range(self.col_index-2, self.col_index+3):
                if 0 <= x <= 7 and 0 <= y <= 7 and BOARD[x][y] != self.position and BOARD[x][y] not in unavailable_moves:
                    available_moves.append(BOARD[x][y])
        return available_moves


class Pawn(Figure):
    def list_available_moves(self) -> list[str]:
        available_moves = []
        if self.row_index == 1:
            available_moves.append(BOARD[self.row_index + 1][self.col_index])
            available_moves.append(BOARD[self.row_index + 2][self.col_index])
        elif self.row_index < 7:
            available_moves.append(BOARD[self.row_index + 1][self.col_index])
        return available_moves


k = King("E1")
print(f'King:{k.list_available_moves()}')

q = Queen("G3")
print(f'Queen: {q.list_available_moves()}')

r = Rook("H2")
print(f'Rook: {r.list_available_moves()}')

b = Bishop("E3")
print(f'Bishop: {b.list_available_moves()}')

kn = Knight("H1")
print(f'Knight: {kn.list_available_moves()}')

p = Pawn("B4")
print(f'Pawn: {p.list_available_moves()}')
