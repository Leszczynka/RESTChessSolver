from abc import ABC, abstractmethod

BOARD = [[letter+number for letter in 'ABCDEFGH'] for number in '12345678']


class Figure(ABC):
    row_index: int
    col_index: int

    def __init__(self, position: str):
        self.position = position

    @abstractmethod
    def list_available_moves(self) -> list[str]:
        pass

    def validate_move(self, dest_field: str) -> bool:
        pass

    def get_index_from_the_board(self):
        self.row_index = [BOARD.index(row) for row in BOARD if self.position in row][0]
        self.col_index = [row.index(self.position) for row in BOARD if self.position in row][0]


class King(Figure):
    def list_available_moves(self) -> list[str]:
        pass


class Queen(Figure):
    def list_available_moves(self) -> list[str]:
        pass


class Rook(Figure):
    def list_available_moves(self) -> list[str]:
        pass


class Bishop(Figure):
    def list_available_moves(self) -> list[str]:
        pass


class Knight(Figure):
    def list_available_moves(self) -> list[str]:
        pass


class Pawn(Figure):
    def list_available_moves(self) -> list[str]:
        pass


print(BOARD)
k = King("C3")
k.get_index_from_the_board()
print(k.row_index)
print(k.col_index)