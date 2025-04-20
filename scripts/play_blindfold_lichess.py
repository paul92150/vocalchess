import chess
from _setup_path import *

from src.voice.recognizer import VoiceRecognizer
from src.voice.tts import TextToSpeech
from src.voice.keyboard_listener import KeyboardListener
from src.game.lichess_moves import LichessMoveFetcher
from src.game.stockfish_engine import StockfishEngine
from src.utils.move_utils import is_valid_uci_move


def main(start_fen=None):
    board = chess.Board(start_fen) if start_fen else chess.Board()

    recognizer = VoiceRecognizer()
    speaker = TextToSpeech()
    listener = KeyboardListener()
    lichess = LichessMoveFetcher(debug=False)
    engine = StockfishEngine(debug=False)

    listener.start()

    print("🧠 Welcome to Vocal Chess (Lichess + Stockfish)!")
    print("Say your moves. Press space to trigger speech recognition.")
    speaker.speak("Welcome to Vocal Chess. Press space and speak your move.")

    while not board.is_game_over():
        print("\nCurrent position:")
        print(board)

        print("[INFO] Waiting for your move...")
        speaker.speak("Your turn. Press space and speak your move.")
        listener.wait_for_space()

        spoken = recognizer.listen_for_move()
        if not spoken:
            speaker.speak("I didn't catch that. Try again.")
            continue

        if not is_valid_uci_move(spoken):
            speaker.speak("Invalid format. Try again.")
            continue

        move = chess.Move.from_uci(spoken)
        if move not in board.legal_moves:
            speaker.speak("Illegal move. Try again.")
            continue

        board.push(move)
        print("[PLAYER] Your move:", move)
        speaker.speak(f"You played {move.uci()}")

        if board.is_game_over():
            break

        # --- Opponent Move: Lichess or Stockfish ---
        fen = board.fen()
        opponent_move = lichess.get_weighted_move(fen)

        if opponent_move:
            move = chess.Move.from_uci(opponent_move)
            board.push(move)
            print("[HUMAN] Played:", move)
            speaker.speak(f"Human move {move.uci()}")
        else:
            print("[INFO] No human data. Switching to Stockfish.")
            move = engine.get_best_move(board)
            board.push(move)
            print("[ENGINE] Stockfish played:", move)
            speaker.speak(f"Engine move {move.uci()}")

    result = board.result()
    print("\nGame over. Result:", result)
    speaker.speak(f"Game over. Result: {result}")
    engine.close()


if __name__ == "__main__":
    main()
