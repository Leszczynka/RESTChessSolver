# REST Chess Solver
A simple Flask REST application that allows you to check the possible moves of each chess figure, and also verifies whether a move is possible for a given figure.
The application has tests developed using pytest. The code was formatted using Black and verified with flake8 linter.
## Table of contents

* [Technology](#technology)
* [Setup and run](#setup-and-run)
* [Endpoints](#endpoints)


### Technology
* Python 3.8
* Flask 2.2
* Pytest
* Black
* Flake8
* Docker*

### Setup and run
Make sure you have a required Python version installed.
1. Clone the repo.
2. Create a virtual environment and activate it:
```bash
python -m venv venv

source venv/bin/activate
```

3. From your command line pointing to the project root directory:

```bash
# Install requirements:
pip install -r requirements.txt

# Run server:
flask run -p 8000 # or 'flask run' to run server on default port 5000
```
*Using Docker:

1. Clone the repo.

2. From your command line pointing to the project root directory:

```bash
# Build an image:
docker build -t chess_flask .

# Run container:
docker run -itd -p 8000:8000 chess_flask
```

### Endpoints

* [GET] /api/v1/{chess-figure}/{current-field} - displays a list of all possible moves
* [GET] /api/v1/{chess-figure}/{current-field}/{dest-field} - validates whether a move to the given field is permitted

Example queries and responses:
```bash
curl http://127.0.0.1:8000/api/v1/king/b2
{
    "availableMoves": [
        "A1",
        "B1",
        "C1",
        "A2",
        "C2",
        "A3",
        "B3",
        "C3"
    ],
    "currentField": "B2",
    "error": null,
    "figure": "king"
}

curl http://127.0.0.1:8000/api/v1/pawn/a2/a4
{
    "currentField": "A2",
    "destField": "A4",
    "error": null,
    "figure": "pawn",
    "move": "valid"
}

```

Endpoints have been also tested in Postman.


