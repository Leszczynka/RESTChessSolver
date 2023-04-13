from flask import Flask, jsonify
from models import King, Queen, Rook, Knight, Bishop, Pawn


app = Flask(__name__)


@app.route('/api/v1/<string:chess_figure>/<string:current_field>', methods=['GET'])
def get_available_moves(chess_figure: str, current_field: str):
    moves = []
    error = None
    response_code = None
    field = verify_field(current_field)
    figure = verify_figure(chess_figure)
    if not field:
        error = 'Field does not exist.'
        response_code = 409
    elif not figure:
        error = 'Figure does not exist.'
        response_code = 404
    elif field and figure:
        moves = figure(current_field.upper()).list_available_moves()
        error = 'null'
        response_code = 200

    return jsonify(
        {
            "availableMoves": moves,
            "error": error,
            "figure": chess_figure.lower(),
            "currentField": current_field.upper()
        }
    ), response_code


@app.route('/api/v1/<string:chess_figure>/<string:current_field>/<string:dest_field>', methods=['GET'])
def validate_move(chess_figure: str, current_field: str, dest_field: str):
    error = None
    response_code = None
    move = 'invalid'
    c_field = verify_field(current_field)
    d_field = verify_field(dest_field)
    figure = verify_figure(chess_figure)
    if not c_field or not d_field:
        error = 'Field does not exist.'
        response_code = 409
    elif not figure:
        error = 'Figure does not exist.'
        response_code = 404
    elif c_field and d_field and figure:
        move = figure(current_field.upper()).validate_move(dest_field.upper())
        if move:
            move = 'valid'
            error = 'null'

        else:
            move = 'invalid'
            error = 'Current move is not permitted.'

        response_code = 200

    return jsonify(
        {
            "move": move,
            "error": error,
            "figure": chess_figure.lower(),
            "currentField": current_field.upper(),
            "destField": dest_field.upper(),
        }
    ), response_code


def verify_figure(chess_figure: str):
    match chess_figure.capitalize():
        case 'King':
            figure = King
        case 'Queen':
            figure = Queen
        case 'Rook':
            figure = Rook
        case 'Bishop':
            figure = Bishop
        case 'Knight':
            figure = Knight
        case 'Pawn':
            figure = Pawn
        case _:
            figure = False
    return figure


def verify_field(field: str):
    return field[0].upper() in 'ABCDEFGH' and field[1] in '12345678' and len(field) == 2


if __name__ == '__main__':
    app.run(debug=True, port=8000)
