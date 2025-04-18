import re

def is_valid_uci_move(move_str):
    """
    Validate if a move string matches the UCI format (e.g., 'e2e4', 'g1f3', 'e7e8q').
    Returns True if it matches, False otherwise.
    """
    # UCI move format is always 4 characters (from + to), optional promotion (like 'q', 'r', etc.)
    pattern = r"^[a-h][1-8][a-h][1-8][qrbn]?$"
    return re.match(pattern, move_str) is not None