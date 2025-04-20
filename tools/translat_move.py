import chess
from _setup_path    import *
from src.translator.move_translator import find_uci_move

def test_translations():
    tests = [
        ("Knight to f3", "g1f3", chess.STARTING_FEN),
        ("Knight takes d4", "c6d4", "r1bqkbnr/pppppppp/2n5/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq - 0 3"),
        ("e4", "e2e4", chess.STARTING_FEN),
        ("d takes e5", "d4e5", "rnbqkbnr/pppp1ppp/8/4p3/3P4/8/PPP2PPP/RNBQKBNR w KQkq e6 0 3"),
        ("e takes d4", "e3d4", "rnbqkbnr/pppppppp/8/8/3p4/4P3/PPP2PPP/RNBQKBNR w KQkq - 0 3"),
        ("bishop to c4", "f1c4", "rnbqkbnr/pppppppp/8/8/3p4/4P3/PPP2PPP/RNBQKBNR w KQkq - 0 3"),
        ("bishop takes f6", "g5f6", "rnbqkb1r/pppp1ppp/5n2/6B1/4P3/8/PPPP1PPP/RN1QKBNR w KQkq - 2 4"),
        ("castle kingside", "e1g1", "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQK2R w KQkq - 0 1"),
        ("castle queenside", "e1c1", "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/R3KBNR w KQkq - 0 1"),
        ("rook to d1", "a1d1", "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/R3KBNR w KQkq - 0 1"),
        ("queen to h5", "d1h5", "rnbqkbnr/pppppppp/8/8/3p4/4P3/PPP2PPP/RNBQKBNR w KQkq - 0 3"),
        ("knight takes f6", "g4f6", "rnbqkb1r/pppppppp/5n2/8/6N1/8/PPPPPPPP/RNBQKB1R w KQkq - 0 1"),
        ("pawn to a4", "a2a4", chess.STARTING_FEN),
        ("g takes h6", "g5h6", "rnbqkbnr/pppppppp/7p/6P1/8/8/PPPPP1PP/RNBQKBNR w KQkq - 0 1"),
    ]

    passed = 0
    for text, expected_uci, fen in tests:
        board = chess.Board(fen)
        result = find_uci_move(board, text)
        if result == expected_uci:
            print(f"✅ PASSED: {text} -> {result}")
            passed += 1
        else:
            print(f"❌ FAILED: {text} -> {result} (expected {expected_uci})")

    print(f"\n{passed}/{len(tests)} tests passed.")

test_translations()
