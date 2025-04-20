import pygame
import chess
from _setup_path import *
from src.ui.board_display import (
    draw_board,
    draw_pieces,
    load_piece_surfaces
)
from src.game.stockfish_engine import StockfishEngine
from src.game.fen_presets import FEN_PRESETS

# Constants
WIDTH, HEIGHT = 950, 750
SQ_SIZE = HEIGHT // 8
FPS = 30
SIDEBAR_WIDTH = 200

def draw_sidebar(screen, game_count, time_limit, depth_limit, use_time_limit):
    pygame.draw.rect(screen, (255, 255, 255), (WIDTH - SIDEBAR_WIDTH, 0, SIDEBAR_WIDTH, HEIGHT))
    font = pygame.font.SysFont('Arial', 24)

    # Labels
    game_label = font.render("Games", True, (0, 0, 0))
    count_label = font.render(str(game_count), True, (0, 0, 0))
    mode_label = font.render("MODE: TIME" if use_time_limit else "MODE: DEPTH", True, (255, 0, 0))
    time_label = font.render(f"←/→ time: {time_limit:.2f}s", True, (0, 0, 0))
    depth_label = font.render(f"↑/↓ depth: {depth_limit}", True, (0, 0, 0))
    toggle_label = font.render("T: toggle mode", True, (0, 0, 0))

    # Positions
    screen.blit(game_label, (WIDTH - SIDEBAR_WIDTH + 10, 10))
    screen.blit(count_label, (WIDTH - SIDEBAR_WIDTH + 10, 40))
    screen.blit(mode_label, (WIDTH - SIDEBAR_WIDTH + 10, 80))
    screen.blit(time_label, (WIDTH - SIDEBAR_WIDTH + 10, 120))
    screen.blit(depth_label, (WIDTH - SIDEBAR_WIDTH + 10, 150))
    screen.blit(toggle_label, (WIDTH - SIDEBAR_WIDTH + 10, 190))

    # Undo button
    undo_button = pygame.Rect(WIDTH - SIDEBAR_WIDTH + 10, 240, SIDEBAR_WIDTH - 20, 40)
    pygame.draw.rect(screen, (200, 0, 0), undo_button)
    undo_text = font.render("Undo Move", True, (255, 255, 255))
    screen.blit(undo_text, (undo_button.x + 5, undo_button.y + 5))

    return undo_button


def main(start_fen=None):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Play Stockfish with Tuning")
    clock = pygame.time.Clock()

    stockfish = StockfishEngine()
    piece_surfaces = load_piece_surfaces()
    board = chess.Board(start_fen if start_fen else None)
    selected_piece = None
    valid_moves = []
    position_history = [board.fen()]
    game_count = 0

    # Tuning
    time_limit = 2.0
    depth_limit = 10
    use_time_limit = True

    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_board(screen, game_count)
        draw_pieces(screen, board, piece_surfaces, selected_piece)
        undo_button = draw_sidebar(screen, game_count, time_limit, depth_limit, use_time_limit)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        if time_limit > 0.2:
                            time_limit = round(time_limit - 0.1, 2)
                        elif time_limit > 0.01:
                            time_limit = round(time_limit - 0.01, 3)
                        time_limit = max(0.01, time_limit)

                elif event.key == pygame.K_RIGHT:
                    if time_limit < 0.05:
                        time_limit = round(time_limit + 0.005, 4)
                    elif time_limit < 0.2:
                        time_limit = round(time_limit + 0.01, 3)
                    else:
                        time_limit = round(time_limit + 0.1, 2)

                elif event.key == pygame.K_UP:
                    depth_limit += 1
                elif event.key == pygame.K_DOWN:
                    depth_limit = max(1, depth_limit - 1)
                elif event.key == pygame.K_t:
                    use_time_limit = not use_time_limit

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                if undo_button.collidepoint((mouse_x, mouse_y)):
                    if len(position_history) > 1:
                        position_history.pop()
                        board.set_fen(position_history[-1])
                    continue  # Skip rest of logic

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

                        if use_time_limit:
                            engine_move = stockfish.get_best_move(board, time_limit=time_limit)
                        else:
                            engine_move = stockfish.get_best_move(board, depth_limit=depth_limit)

                        if engine_move:
                            board.push(engine_move)
                            position_history.append(board.fen())

                    selected_piece = None
                    valid_moves = []

        pygame.display.flip()
        clock.tick(FPS)

    stockfish.close()
    pygame.quit()

if __name__ == "__main__":
    main(FEN_PRESETS["initial_position"])
