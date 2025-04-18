import chess
from _setup_path import *
from src.voice.recognizer import VoiceRecognizer
from src.voice.tts import TextToSpeech
from src.voice.keyboard_listener import KeyboardListener
from src.game.stockfish_engine import StockfishEngine 
from src.utils.move_utils import is_valid_uci_move

def main():
    recognizer = VoiceRecognizer()
    speaker = TextToSpeech()
    listener = KeyboardListener() 
    listener.start()

    stockfish = StockfishEngine()

    board = chess.Board()

    print("Welcome to Vocal Chess! Press space to speak your move.")
    speaker.speak("Welcome to vocal chess.")
 
    while not board.is_game_over():
        print("\nCurrent FEN:", board.fen())
        print(board)

        listener.wait_for_space()
        move_str = recognizer.listen_for_move()

        if not move_str:
            speaker.speak("I didn't catch that. Please try again.")
            continue

        if not is_valid_uci_move(move_str):
            speaker.speak("Invalid move format.")
            continue

        move = chess.Move.from_uci(move_str)

        if move in board.legal_moves:
            board.push(move)
            print(f"You played: {move}")
        else:
            speaker.speak("Illegal move. Try again.")
            continue

        # Stockfish plays next
        if board.is_game_over():
            break
        engine_move = stockfish.get_best_move(board)
        board.push(engine_move)
        print(f"Engine played: {engine_move}")
        speaker.speak(f"Engine plays {engine_move.uci()}")

    result = board.result()
    print("Game over. Result:", result)
    speaker.speak(f"Game over. Result {result}")
    stockfish.close()

if __name__ == "__main__":
    main()