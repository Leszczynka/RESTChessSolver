from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, position: str):
        self.position = position

    @abstractmethod
    def list_available_moves(self) -> list[str]:
        pass

    def validate_move(self, dest_field: str) -> bool:
        pass


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

