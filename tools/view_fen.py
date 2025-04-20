import pygame
import chess
import sys

from _setup_path import *
from src.ui.board_display import draw_board, draw_pieces, load_piece_surfaces

# Constants
WIDTH, HEIGHT = 900, 750
SQ_SIZE = HEIGHT // 8
FPS = 30

def view_fen(fen):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("FEN Viewer")
    clock = pygame.time.Clock()

    board = chess.Board(fen)
    surfaces = load_piece_surfaces()

    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_board(screen, 0)  # No game count needed
        draw_pieces(screen, board, surfaces)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    # Default to starting position if no FEN is passed
    if len(sys.argv) > 1:
        fen_input = " ".join(sys.argv[1:])
    else:
        fen_input = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQK2R w KQkq - 0 1"

    view_fen(fen_input)
