import chess
import chess.engine

class StockfishEngine:
    def __init__(self, path="/opt/homebrew/bin/stockfish", debug=False):
        self.path = path
        self.debug = debug
        self.engine = chess.engine.SimpleEngine.popen_uci(self.path)

    def get_best_move(self, board, time_limit=None, depth_limit=None):
        """Returns the best move using either time or depth."""
        if time_limit is not None:
            limit = chess.engine.Limit(time=time_limit)
        elif depth_limit is not None:
            limit = chess.engine.Limit(depth=depth_limit)
        else:
            limit = chess.engine.Limit(time=2.0)  # Default fallback

        result = self.engine.play(board, limit)
        if self.debug:
            print(f"[DEBUG] Stockfish move: {result.move}")
        return result.move

    def close(self):
        if self.debug:
            print("[DEBUG] Closing Stockfish engine.")
        self.engine.quit()
