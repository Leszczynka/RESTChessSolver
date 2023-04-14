import pytest
from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_get_available_moves_with_invalid_field(client):
    response = client.get("http://127.0.0.1:8000/api/v1/king/h15")
    data_json = response.get_json()
    assert data_json["availableMoves"] == []
    assert data_json["error"] == "Field does not exist."
    assert data_json["figure"] == "king"
    assert data_json["currentField"] == "H15"
    assert response.status_code == 409


def test_get_available_moves_with_invalid_figure(client):
    response = client.get("http://127.0.0.1:8000/api/v1/kong/e3")
    data_json = response.get_json()
    assert data_json["availableMoves"] == []
    assert data_json["error"] == "Figure does not exist."
    assert data_json["figure"] == "kong"
    assert data_json["currentField"] == "E3"
    assert response.status_code == 404


def test_king_get_available_moves_with_valid_data(client):
    response = client.get("http://127.0.0.1:8000/api/v1/king/e3")
    data_json = response.get_json()
    assert data_json["availableMoves"] == [
        "D2",
        "E2",
        "F2",
        "D3",
        "F3",
        "D4",
        "E4",
        "F4",
    ]
    assert data_json["error"] is None
    assert data_json["figure"] == "king"
    assert data_json["currentField"] == "E3"
    assert response.status_code == 200


def test_queen_get_available_moves_with_valid_data(client):
    response = client.get("http://127.0.0.1:8000/api/v1/queen/b3")
    data_json = response.get_json()
    assert data_json["availableMoves"] == [
        "A3",
        "C3",
        "D3",
        "E3",
        "F3",
        "G3",
        "H3",
        "B1",
        "B2",
        "B4",
        "B5",
        "B6",
        "B7",
        "B8",
        "D1",
        "A2",
        "C2",
        "A4",
        "C4",
        "D5",
        "E6",
        "F7",
        "G8",
    ]
    assert data_json["error"] is None
    assert data_json["figure"] == "queen"
    assert data_json["currentField"] == "B3"
    assert response.status_code == 200


def test_rook_get_available_moves_with_valid_data(client):
    response = client.get("http://127.0.0.1:8000/api/v1/rook/a2")
    data_json = response.get_json()
    assert data_json["availableMoves"] == [
        "B2",
        "C2",
        "D2",
        "E2",
        "F2",
        "G2",
        "H2",
        "A1",
        "A3",
        "A4",
        "A5",
        "A6",
        "A7",
        "A8",
    ]
    assert data_json["error"] is None
    assert data_json["figure"] == "rook"
    assert data_json["currentField"] == "A2"
    assert response.status_code == 200


def test_bishop_get_available_moves_with_valid_data(client):
    response = client.get("http://127.0.0.1:8000/api/v1/bishop/d6")
    data_json = response.get_json()
    assert data_json["availableMoves"] == [
        "H2",
        "A3",
        "G3",
        "B4",
        "F4",
        "C5",
        "E5",
        "C7",
        "E7",
        "B8",
        "F8",
    ]
    assert data_json["error"] is None
    assert data_json["figure"] == "bishop"
    assert data_json["currentField"] == "D6"
    assert response.status_code == 200


def test_knight_get_available_moves_with_valid_data(client):
    response = client.get("http://127.0.0.1:8000/api/v1/knight/f1")
    data_json = response.get_json()
    assert data_json["availableMoves"] == ["D2", "H2", "E3", "G3"]
    assert data_json["error"] is None
    assert data_json["figure"] == "knight"
    assert data_json["currentField"] == "F1"
    assert response.status_code == 200


def test_pawn_get_available_moves_with_valid_data(client):
    response = client.get("http://127.0.0.1:8000/api/v1/pawn/b2")
    data_json = response.get_json()
    assert data_json["availableMoves"] == ["B3", "B4"]
    assert data_json["error"] is None
    assert data_json["figure"] == "pawn"
    assert data_json["currentField"] == "B2"
    assert response.status_code == 200


def test_validate_move_with_invalid_current_field(client):
    response = client.get("http://127.0.0.1:8000/api/v1/king/h15/h8")
    data_json = response.get_json()
    assert data_json["move"] == "invalid"
    assert data_json["error"] == "Field does not exist."
    assert data_json["figure"] == "king"
    assert data_json["currentField"] == "H15"
    assert data_json["destField"] == "H8"
    assert response.status_code == 409


def test_validate_move_with_invalid_dest_field(client):
    response = client.get("http://127.0.0.1:8000/api/v1/king/h8/h15")
    data_json = response.get_json()
    assert data_json["move"] == "invalid"
    assert data_json["error"] == "Field does not exist."
    assert data_json["figure"] == "king"
    assert data_json["currentField"] == "H8"
    assert data_json["destField"] == "H15"
    assert response.status_code == 409


def test_validate_move_with_invalid_figure(client):
    response = client.get("http://127.0.0.1:8000/api/v1/kong/e3/e4")
    data_json = response.get_json()
    assert data_json["move"] == "invalid"
    assert data_json["error"] == "Figure does not exist."
    assert data_json["figure"] == "kong"
    assert data_json["currentField"] == "E3"
    assert data_json["destField"] == "E4"
    assert response.status_code == 404


def test_king_validate_move_with_invalid_move(client):
    response = client.get("http://127.0.0.1:8000/api/v1/king/e3/d6")
    data_json = response.get_json()
    assert data_json["move"] == "invalid"
    assert data_json["error"] == "Current move is not permitted."
    assert data_json["figure"] == "king"
    assert data_json["currentField"] == "E3"
    assert data_json["destField"] == "D6"
    assert response.status_code == 200


def test_king_validate_move_with_valid_move(client):
    response = client.get("http://127.0.0.1:8000/api/v1/king/e3/d2")
    data_json = response.get_json()
    assert data_json["move"] == "valid"
    assert data_json["error"] is None
    assert data_json["figure"] == "king"
    assert data_json["currentField"] == "E3"
    assert data_json["destField"] == "D2"
    assert response.status_code == 200


def test_queen_validate_move_with_invalid_move(client):
    response = client.get("http://127.0.0.1:8000/api/v1/queen/e3/d6")
    data_json = response.get_json()
    assert data_json["move"] == "invalid"
    assert data_json["error"] == "Current move is not permitted."
    assert data_json["figure"] == "queen"
    assert data_json["currentField"] == "E3"
    assert data_json["destField"] == "D6"
    assert response.status_code == 200


def test_queen_validate_move_with_valid_move(client):
    response = client.get("http://127.0.0.1:8000/api/v1/queen/e3/d2")
    data_json = response.get_json()
    assert data_json["move"] == "valid"
    assert data_json["error"] is None
    assert data_json["figure"] == "queen"
    assert data_json["currentField"] == "E3"
    assert data_json["destField"] == "D2"
    assert response.status_code == 200


def test_rook_validate_move_with_invalid_move(client):
    response = client.get("http://127.0.0.1:8000/api/v1/rook/e3/d6")
    data_json = response.get_json()
    assert data_json["move"] == "invalid"
    assert data_json["error"] == "Current move is not permitted."
    assert data_json["figure"] == "rook"
    assert data_json["currentField"] == "E3"
    assert data_json["destField"] == "D6"
    assert response.status_code == 200


def test_rook_validate_move_with_valid_move(client):
    response = client.get("http://127.0.0.1:8000/api/v1/rook/e3/d3")
    data_json = response.get_json()
    assert data_json["move"] == "valid"
    assert data_json["error"] is None
    assert data_json["figure"] == "rook"
    assert data_json["currentField"] == "E3"
    assert data_json["destField"] == "D3"
    assert response.status_code == 200


def test_bishop_validate_move_with_invalid_move(client):
    response = client.get("http://127.0.0.1:8000/api/v1/bishop/e3/d6")
    data_json = response.get_json()
    assert data_json["move"] == "invalid"
    assert data_json["error"] == "Current move is not permitted."
    assert data_json["figure"] == "bishop"
    assert data_json["currentField"] == "E3"
    assert data_json["destField"] == "D6"
    assert response.status_code == 200


def test_bishop_validate_move_with_valid_move(client):
    response = client.get("http://127.0.0.1:8000/api/v1/bishop/e3/d4")
    data_json = response.get_json()
    assert data_json["move"] == "valid"
    assert data_json["error"] is None
    assert data_json["figure"] == "bishop"
    assert data_json["currentField"] == "E3"
    assert data_json["destField"] == "D4"
    assert response.status_code == 200


def test_knight_validate_move_with_invalid_move(client):
    response = client.get("http://127.0.0.1:8000/api/v1/knight/e3/d6")
    data_json = response.get_json()
    assert data_json["move"] == "invalid"
    assert data_json["error"] == "Current move is not permitted."
    assert data_json["figure"] == "knight"
    assert data_json["currentField"] == "E3"
    assert data_json["destField"] == "D6"
    assert response.status_code == 200


def test_knight_validate_move_with_valid_move(client):
    response = client.get("http://127.0.0.1:8000/api/v1/knight/e3/d5")
    data_json = response.get_json()
    assert data_json["move"] == "valid"
    assert data_json["error"] is None
    assert data_json["figure"] == "knight"
    assert data_json["currentField"] == "E3"
    assert data_json["destField"] == "D5"
    assert response.status_code == 200


def test_pawn_validate_move_with_invalid_move(client):
    response = client.get("http://127.0.0.1:8000/api/v1/pawn/e3/d6")
    data_json = response.get_json()
    assert data_json["move"] == "invalid"
    assert data_json["error"] == "Current move is not permitted."
    assert data_json["figure"] == "pawn"
    assert data_json["currentField"] == "E3"
    assert data_json["destField"] == "D6"
    assert response.status_code == 200


def test_pawn_validate_move_with_valid_move(client):
    response = client.get("http://127.0.0.1:8000/api/v1/pawn/e3/e4")
    data_json = response.get_json()
    assert data_json["move"] == "valid"
    assert data_json["error"] is None
    assert data_json["figure"] == "pawn"
    assert data_json["currentField"] == "E3"
    assert data_json["destField"] == "E4"
    assert response.status_code == 200
