import pygame
import chess
from _setup_path import *
from src.ui.board_display import (
    draw_board,
    draw_pieces,
    draw_sidebar,
    load_piece_surfaces
)
from src.game.lichess_moves import LichessMoveFetcher
from src.game.stockfish_engine import StockfishEngine
from src.game.fen_presets import FEN_PRESETS

# Constants
WIDTH, HEIGHT = 900, 750
SQ_SIZE = HEIGHT // 8
FPS = 30

def main(start_fen=None):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Play Humans, Then Stockfish")
    clock = pygame.time.Clock()

    # Initialize helpers
    lichess = LichessMoveFetcher()
    stockfish = StockfishEngine()
    piece_surfaces = load_piece_surfaces()

    # Game state
    board = chess.Board(start_fen if start_fen else None)
    selected_piece = None
    valid_moves = []
    game_count = 0
    position_history = [board.fen()]

    running = True
    while running:
        draw_board(screen, game_count)
        draw_pieces(screen, board, piece_surfaces, selected_piece)
        undo_button = draw_sidebar(screen, game_count)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                if undo_button.collidepoint(event.pos):
                    if len(position_history) > 1:
                        position_history.pop()
                        board.set_fen(position_history[-1])
                        game_count = lichess.get_game_count(board.fen())
                        selected_piece = None
                        valid_moves = []
                    continue

                col = mouse_x // SQ_SIZE
                row = mouse_y // SQ_SIZE
                square = chess.square(col, 7 - row)

                if selected_piece is None:
                    if board.piece_at(square) and board.piece_at(square).color == board.turn:
                        selected_piece = square
                        valid_moves = [move for move in board.legal_moves if move.from_square == square]
                else:
                    move = chess.Move(selected_piece, square)
                    if move in valid_moves:
                        position_history.append(board.fen())
                        board.push(move)
                        game_count = lichess.get_game_count(board.fen())

                        # Computer move
                        if game_count == 0:
                            engine_move = stockfish.get_best_move(board)
                        else:
                            engine_move = lichess.get_weighted_move(board.fen())

                        if engine_move:
                            board.push(chess.Move.from_uci(str(engine_move)))
                            position_history.append(board.fen())
                            game_count = lichess.get_game_count(board.fen())

                    selected_piece = None
                    valid_moves = []

        pygame.display.flip()
        clock.tick(FPS)

    stockfish.close()
    pygame.quit()

if __name__ == "__main__":
    # You can swap the opening here
    main(FEN_PRESETS["initial_position"])
