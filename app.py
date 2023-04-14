from flask import Flask, jsonify
from typing import List
from models import King, Queen, Rook, Knight, Bishop, Pawn


app = Flask(__name__)


@app.route("/api/v1/<string:chess_figure>/<string:current_field>", methods=["GET"])
def get_available_moves(chess_figure: str, current_field: str):
    moves: List[str] = []
    current_field = current_field.upper()
    field = verify_field(current_field)
    figure = verify_figure(chess_figure)
    if not field:
        error = "Field does not exist."
        response_code = 409
    elif not figure:
        error = "Figure does not exist."
        response_code = 404
    else:
        moves = figure(current_field).list_available_moves()
        error = None
        response_code = 200

    return (
        jsonify(
            {
                "availableMoves": moves,
                "error": error,
                "figure": chess_figure.lower(),
                "currentField": current_field,
            }
        ),
        response_code,
    )


@app.route(
    "/api/v1/<string:chess_figure>/<string:current_field>/<string:dest_field>",
    methods=["GET"],
)
def validate_move(chess_figure: str, current_field: str, dest_field: str):
    move = "invalid"
    figure = verify_figure(chess_figure)
    current_field = current_field.upper()
    dest_field = dest_field.upper()

    if not verify_field(current_field) or not verify_field(dest_field):
        error = "Field does not exist."
        response_code = 409
    elif not figure:
        error = "Figure does not exist."
        response_code = 404
    else:
        move = figure(current_field).validate_move(dest_field)
        response_code = 200
        if move:
            error = None
            move = "valid"
        else:
            error = "Current move is not permitted."
            move = "invalid"

    return (
        jsonify(
            {
                "move": move,
                "error": error,
                "figure": chess_figure.lower(),
                "currentField": current_field,
                "destField": dest_field,
            }
        ),
        response_code,
    )


def verify_figure(chess_figure: str):
    match chess_figure.capitalize():
        case "King":
            figure = King
        case "Queen":
            figure = Queen
        case "Rook":
            figure = Rook
        case "Bishop":
            figure = Bishop
        case "Knight":
            figure = Knight
        case "Pawn":
            figure = Pawn
        case _:
            figure = None
    return figure


def verify_field(field: str) -> bool:
    return field[0] in "ABCDEFGH" and field[1] in "12345678" and len(field) == 2


if __name__ == "__main__":
    app.run(debug=True, port=8000)
