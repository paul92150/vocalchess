# src/game/move_utils.py

"""
Utility functions for parsing, validating, and converting chess moves.
"""

import chess

def is_valid_uci_move(move_str: str, board: chess.Board) -> bool:
    """
    Checks if the given UCI move is legal on the current board.
    """
    try:
        move = chess.Move.from_uci(move_str)
        return move in board.legal_moves
    except ValueError:
        return False


def parse_spoken_move(spoken: str) -> str | None:
    """
    Converts spoken input into UCI move format, e.g.:
    'e2 to e4' → 'e2e4'
    'free to e4' → 'f3e4' (corrected for speech recognition errors)
    """
    spoken = spoken.lower().replace(" to ", "").replace("free", "3").replace(" ", "")
    if len(spoken) == 4 and all(c in "abcdefgh12345678" for c in spoken):
        return spoken
    return None


def get_legal_moves_uci(board: chess.Board) -> list[str]:
    """
    Returns a list of all legal moves in UCI format for the current board state.
    """
    return [move.uci() for move in board.legal_moves]


def describe_move(move: chess.Move) -> str:
    """
    Returns a basic verbal description of a move.
    """
    return f"{move.uci()[0:2]} to {move.uci()[2:4]}"
