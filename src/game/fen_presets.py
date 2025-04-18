# src/game/fen_presets.py

"""
FEN presets and utilities for predefined chess openings or custom positions.
"""

FEN_PRESETS = {
    "initial_position": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
    "halloween_gambit": "r1bqkb1r/pppppppp/2n2n2/4p3/4P3/2N2N2/PPPP1PPP/R1BQKB1R w KQkq - 4 4",
    # Add more presets here
}


def get_fen(name: str) -> str:
    """
    Get a FEN string by name. Defaults to initial position.
    """
    return FEN_PRESETS.get(name, FEN_PRESETS["initial"])


def list_presets() -> list:
    """
    List available preset names.
    """
    return list(FEN_PRESETS.keys())
