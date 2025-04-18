import chess
import chess.engine

class StockfishEngine:
    def __init__(self, path="/opt/homebrew/bin/stockfish", thinking_time=2.0, debug=False):
        self.path = path
        self.thinking_time = thinking_time
        self.debug = debug
        self.engine = chess.engine.SimpleEngine.popen_uci(self.path)

    def get_best_move(self, board):
        """Returns the best move found by Stockfish from the current position."""
        result = self.engine.play(board, chess.engine.Limit(time=self.thinking_time))
        if self.debug:
            print(f"[DEBUG] Stockfish move: {result.move}")
        return result.move

    def close(self):
        """Properly closes the engine process."""
        if self.debug:
            print("[DEBUG] Closing Stockfish engine.")
        self.engine.quit()
