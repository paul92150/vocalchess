import chess

PIECE_NAMES = {
    "pawn": chess.PAWN,
    "knight": chess.KNIGHT,
    "bishop": chess.BISHOP,
    "rook": chess.ROOK,
    "queen": chess.QUEEN,
    "king": chess.KING
}

def normalize_square(text):
    replacements = {
        " one": "1", " two": "2", " three": "3", " four": "4",
        " five": "5", " six": "6", " seven": "7", " eight": "8"
    }
    for word, digit in replacements.items():
        text = text.replace(word, digit)
    return text

def find_uci_move(board, spoken_text):
    spoken_text = spoken_text.lower().strip()
    spoken_text = normalize_square(spoken_text)

    # === Handle castling ===
    if "castle kingside" in spoken_text or "short castle" in spoken_text:
        for move in board.legal_moves:
            if board.is_kingside_castling(move):
                return move.uci()

    if "castle queenside" in spoken_text or "long castle" in spoken_text:
        for move in board.legal_moves:
            if board.is_queenside_castling(move):
                return move.uci()

    # === Parse regular moves ===
    if " takes " in spoken_text or " captures " in spoken_text:
        for sep in [" takes ", " captures "]:
            if sep in spoken_text:
                parts = spoken_text.split(sep)
                origin_hint = parts[0].strip()
                dest_str = parts[1].strip().replace(" ", "")
                break
    elif " to " in spoken_text:
        parts = spoken_text.split(" to ")
        origin_hint = parts[0].strip()
        dest_str = parts[1].strip().replace(" ", "")
    else:
        tokens = spoken_text.split()
        dest_str = tokens[-1].replace(" ", "")
        origin_hint = " ".join(tokens[:-1])

    try:
        dest = chess.parse_square(dest_str)
    except:
        return None

    piece_type = None
    for name in PIECE_NAMES:
        if name in origin_hint:
            piece_type = PIECE_NAMES[name]
            break

    legal_moves = list(board.legal_moves)
    candidates = []

    for move in legal_moves:
        if move.to_square != dest:
            continue

        from_square = move.from_square
        from_file = chess.square_file(from_square)

        if piece_type is not None:
            if board.piece_type_at(from_square) == piece_type:
                candidates.append(move)
        else:
            # Handle pawn capture like "e takes d4"
            if len(origin_hint) == 1 and origin_hint.isalpha():
                if from_file == ord(origin_hint) - ord("a") and board.piece_type_at(from_square) == chess.PAWN:
                    candidates.append(move)
            else:
                candidates.append(move)

    if len(candidates) == 1:
        return candidates[0].uci()
    else:
        return None



