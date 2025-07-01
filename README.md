# VocalChess - Voice-Controlled Blindfold Chess Interface

**VocalChess** is an experimental project exploring voice-based blindfold chess through speech recognition, natural language processing, and chess engine integration. The system enables players to make chess moves entirely by voice, without visual feedback, simulating blindfolded play against engines and statistically common human openings.

Originally developed as a personal exploration, VocalChess demonstrates applied skills in real-time input parsing, rule-based systems, NLP, and human-computer interaction, relevant to domains like algorithmic trading, research systems, and decision-making under uncertainty.

## Overview

VocalChess includes several experimental gameplay modes:
- Vocal Blindfold Mode: Play against Stockfish using only speech input and audio feedback.
- Human-Then-Engine Mode: Play against statistically common human moves (scraped from Lichess); fallback to Stockfish beyond book.
- Tunable Engine Mode: Dynamically adjust Stockfish’s search depth or time to simulate variable opponent strength.
- Natural Language Translator: Convert spoken or typed instructions like "knight takes f6" into legal UCI moves, based on current board state.
- FEN Visualizer: Display board positions from arbitrary FEN strings in a minimal graphical interface.

## Core Features

- Fully voice-controlled blindfold chess experience via speech-to-text and text-to-speech.
- Hybrid decision logic: human openings from Lichess Explorer combined with fallback to Stockfish.
- Natural language understanding for flexible move input.
- Real-time board validation and error handling.
- Tunable engine difficulty for customized gameplay.
- Debugging tools for FEN testing and move translation.

## Project Structure

```text
vocalchess/
├── assets/
│   └── pieces/                  ← SVG pieces for GUI
├── scripts/
│   ├── play_graphic.py          ← Click-to-play humans then Stockfish
│   ├── play_vocal.py            ← Vocal blindfold mode
│   ├── play_blindfold_lichess.py← WIP: vocal vs human openings
│   ├── play_stockfish_tuned.py  ← Stockfish with tunable difficulty
│   └── _setup_path.py           ← Adds src/ to PYTHONPATH
├── tools/
│   ├── translate_move.py        ← Test natural language move parsing
│   └── view_fen.py              ← Visualize FEN in GUI
├── src/
│   ├── game/
│   │   ├── lichess_moves.py     ← Lichess API integration
│   │   ├── stockfish_engine.py  ← Stockfish interface
│   │   └── fen_presets.py       ← Known opening FENs
│   ├── translator/
│   │   └── move_translator.py   ← Natural language to UCI parser
│   ├── voice/
│   │   ├── recognizer.py        ← Speech recognition
│   │   ├── tts.py               ← Text-to-speech output
│   │   └── keyboard_listener.py ← Voice trigger (space bar)
│   ├── ui/
│   │   └── board_display.py     ← GUI board rendering (Pygame)
│   └── utils/
│       └── move_utils.py        ← Move validation helpers
├── requirements.txt
└── README.md
```

## Installation

```bash
git clone https://github.com/paul92150/vocalchess.git
cd vocalchess
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Make sure `stockfish` is installed and available in your system PATH. You can modify its path in `stockfish_engine.py` if needed.

## How to Use

### Blindfold Vocal Mode

```bash
python scripts/play_vocal.py
```

Press space to speak your move.  
Example commands: "knight to f3", "e takes d4", "castle kingside".  
All moves (yours and engine's) are read aloud.

### Human Openings Then Stockfish

```bash
python scripts/play_graphic.py
```

Start by playing against statistically common human moves.  
When out-of-book, Stockfish takes over.

### Tunable Stockfish Mode

```bash
python scripts/play_stockfish_tuned.py
```

Adjust difficulty using arrow keys:  
← / → to modify time limit  
↑ / ↓ to modify search depth  
Press T to toggle between the two modes

### Tools

Move Translator Tester:

```bash
python tools/translate_move.py
```

FEN Visualizer:

```bash
python tools/view_fen.py
```

## Example Commands

| Spoken Input        | UCI Output |
|---------------------|------------|
| "Knight to f3"      | g1f3       |
| "e takes d4"        | e3d4       |
| "castle kingside"   | e1g1       |
| "bishop takes f6"   | g5f6       |
| "pawn to a4"        | a2a4       |

## Requirements

Main dependencies:
- python-chess
- pygame
- speechrecognition
- pyttsx3
- requests
- cairosvg

All packages are listed in `requirements.txt`.

## Roadmap

- Unify vocal and human-opening logic into one seamless blindfold mode.
- Improve natural language robustness and ambiguity handling.
- Add support for other engines (Leela, Torch, etc.).
- Enable PGN export, replay, and training features.
- Add online mode with Lichess/Chess.com API integration.

## Author

**Paul Lemaire**  
MSc candidate at CentraleSupélec  
LinkedIn: https://www.linkedin.com/in/paul-lemaire-aa0369289

## Disclaimer

This is a personal, research-oriented project built for learning and experimentation. Contributions are always welcome.

---

## License

MIT License - see `LICENSE` file.
