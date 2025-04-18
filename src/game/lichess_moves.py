import requests
import random

class LichessMoveFetcher:
    def __init__(self, base_url="https://explorer.lichess.ovh/lichess", playouts=100, debug=False):
        self.base_url = base_url
        self.playouts = playouts
        self.debug = debug

    def fetch_moves(self, fen):
        params = {"fen": fen, "playouts": self.playouts}
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            if self.debug:
                print(f"[DEBUG] Lichess API returned: {data}")
            return data.get("moves", [])
        except requests.RequestException as e:
            print(f"[ERROR] Failed to fetch data from Lichess API: {e}")
            return []

    def get_weighted_move(self, fen):
        moves_data = self.fetch_moves(fen)
        moves = []
        weights = []

        for move_info in moves_data:
            move = move_info.get("uci")
            total = move_info.get("white", 0) + move_info.get("black", 0) + move_info.get("draws", 0)
            if move and total > 0:
                moves.append(move)
                weights.append(total)

        if moves:
            selected_move = random.choices(moves, weights=weights, k=1)[0]
            if self.debug:
                print(f"[DEBUG] Selected move: {selected_move}")
            return selected_move
        else:
            if self.debug:
                print("[DEBUG] No human move available. Returning None.")
            return None

    def get_game_count(self, fen):
        """Returns total number of games played from the given position."""
        moves_data = self.fetch_moves(fen)
        count = sum(
            move.get("white", 0) + move.get("black", 0) + move.get("draws", 0)
            for move in moves_data
        )
        if self.debug:
            print(f"[DEBUG] Game count from this position: {count}")
        return count
