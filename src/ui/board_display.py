import os
import pygame
import chess
from io import BytesIO
import cairosvg

# === Constants ===
WIDTH, HEIGHT = 900, 750
SQ_SIZE = HEIGHT // 8
FPS = 30

WHITE = (255, 255, 255)
BLUE = (0, 0, 200)
RED = (255, 0, 0)
SELECTED_COLOR = (255, 255, 0)
FONT_COLOR = (0, 0, 0)
SIDEBAR_WIDTH = 150

# === Piece Loader ===

def load_svg_as_surface(svg_path, size=(SQ_SIZE, SQ_SIZE)):
    """Convert an SVG file to a Pygame surface."""
    png_data = cairosvg.svg2png(url=svg_path, output_width=size[0], output_height=size[1])
    return pygame.image.load(BytesIO(png_data), 'png')

# === Load Piece Surfaces ===

def load_piece_surfaces():
    base_path = os.path.join(os.path.dirname(__file__), "../../assets/pieces")
    surfaces = {
        "bN": load_svg_as_surface(os.path.join(base_path, "Chess-Knight.svg")),
        "wN": load_svg_as_surface(os.path.join(base_path, "Chess-White-Knight.svg")),
        "bB": load_svg_as_surface(os.path.join(base_path, "Chess-Bishop.svg")),
        "wB": load_svg_as_surface(os.path.join(base_path, "Chess-White-Bishop.svg")),
        "bQ": load_svg_as_surface(os.path.join(base_path, "Chess-Queen.svg")),
        "wQ": load_svg_as_surface(os.path.join(base_path, "Chess-White-Queen.svg")),
        "bR": load_svg_as_surface(os.path.join(base_path, "Chess-Rook.svg")),
        "wR": load_svg_as_surface(os.path.join(base_path, "Chess-White-Rook.svg")),
        "bK": load_svg_as_surface(os.path.join(base_path, "Chess-King.svg")),
        "wK": load_svg_as_surface(os.path.join(base_path, "Chess-White-King.svg")),
        "bP": load_svg_as_surface(os.path.join(base_path, "Chess-Pawn.svg")),
        "wP": load_svg_as_surface(os.path.join(base_path, "Chess-White-Pawn.svg")),
    }
    return surfaces

# === Drawing Functions ===

def draw_board(screen, game_count):
    for row in range(8):
        for col in range(8):
            color = RED if game_count == 0 and (row + col) % 2 != 0 else WHITE if (row + col) % 2 == 0 else BLUE
            pygame.draw.rect(screen, color, (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_pieces(screen, board, surfaces, selected_piece=None):
    for square, piece in board.piece_map().items():
        row, col = divmod(square, 8)
        flipped_row = 7 - row
        prefix = 'w' if piece.color == chess.WHITE else 'b'
        key = prefix + piece.symbol().upper()

        if key in surfaces:
            screen.blit(surfaces[key], (col * SQ_SIZE, flipped_row * SQ_SIZE))

        if selected_piece == square:
            pygame.draw.rect(screen, SELECTED_COLOR, (col * SQ_SIZE, flipped_row * SQ_SIZE, SQ_SIZE, SQ_SIZE), 5)

def draw_sidebar(screen, game_count):
    pygame.draw.rect(screen, WHITE, (WIDTH - SIDEBAR_WIDTH, 0, SIDEBAR_WIDTH, HEIGHT))
    font = pygame.font.SysFont('Arial', 28)
    small_font = pygame.font.SysFont('Arial', 22)

    label = font.render('Games', True, FONT_COLOR)
    count = small_font.render(str(game_count), True, FONT_COLOR)

    screen.blit(label, (WIDTH - SIDEBAR_WIDTH + 10, 10))
    screen.blit(count, (WIDTH - SIDEBAR_WIDTH + 10, 50))

    # Draw Undo button
    undo_button = pygame.Rect(WIDTH - SIDEBAR_WIDTH + 10, 100, SIDEBAR_WIDTH - 20, 50)
    pygame.draw.rect(screen, (200, 0, 0), undo_button)
    undo_text = small_font.render('Undo Move', True, FONT_COLOR)
    screen.blit(undo_text, (undo_button.x + 10, undo_button.y + 10))

    return undo_button