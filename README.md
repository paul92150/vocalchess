# ♟️ VocalChess – Play Blindfolded, With Your Voice

**VocalChess** is a fun personal project that explores how to play chess **blindfolded**, using only **your voice** to make moves.

It now includes multiple experimental game modes:
- A **vocal mode** where you play against **Stockfish**, using voice commands and audio feedback.
- A **graphical mode** where you play against the most common **human moves** (scraped from Lichess) until the position is no longer known — then **Stockfish** takes over.
- A **tuned engine mode**, where you play Stockfish with adjustable **depth** or **time limits**.
- A **translator tool**, which converts natural language chess moves like `"knight takes f6"` into UCI moves.
- A **FEN visualizer**, to display board positions from any FEN string.

The goal is to **merge everything** into a seamless experience: play against human openings with your voice, blindfolded — and explore positions naturally.

This is still a **work in progress**, but the core mechanics are solid and open to contribution!

---

## 🎯 Goals

- 🔊 Play chess **without seeing the board**, using **speech recognition**.
- 🧠 Start with **human openings** via the **Lichess Explorer API**.
- ♟️ If no human data is found, fallback to **Stockfish**.
- 🗣️ All moves (yours and engine's) are spoken aloud using **text-to-speech**.
- 🪄 Translate natural language like `"knight takes e5"` into valid moves.
- 🎛️ Adjust Stockfish **difficulty** (time or depth).
- 🧪 Easily test FENs and move parsers with debugging tools.

---

## 🗂️ Project Structure

```
vocalchess/
├── assets/
│   └── pieces/             ← SVG pieces used for graphical version
├── scripts/
│   ├── play_graphic.py           ← Click-to-play humans-then-Stockfish
│   ├── play_vocal.py             ← Blindfold vocal Stockfish mode
│   ├── play_blindfold_lichess.py ← Blindfold vocal vs human openings (WIP)
│   ├── play_stockfish_tuned.py   ← Play vs Stockfish with tunable difficulty
│   └── _setup_path.py            ← Adds src/ to PYTHONPATH
│
├── tools/
│   ├── translate_move.py   ← Test move translation from natural language
│   └── view_fen.py         ← Visualize any FEN using the GUI
│
├── src/
│   ├── game/
│   │   ├── lichess_moves.py       ← Fetch & weight moves from Lichess API
│   │   ├── stockfish_engine.py    ← Interface with Stockfish engine
│   │   └── fen_presets.py         ← FENs for known openings
│   │
│   ├── translator/
│   │   └── move_translator.py     ← Parse speech like "knight takes f6"
│   │
│   ├── voice/
│   │   ├── recognizer.py          ← Speech-to-text
│   │   ├── tts.py                 ← Text-to-speech feedback
│   │   └── keyboard_listener.py  ← Space bar trigger to speak
│   │
│   ├── ui/
│   │   └── board_display.py       ← Render board and sidebar with Pygame
│   │
│   └── utils/
│       └── move_utils.py          ← Move validation helpers
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/paul92150/vocalchess.git
cd vocalchess
```

### 2. (Optional) Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

> Make sure `stockfish` is installed and available in your path, or update `stockfish_engine.py`.

---

## 🎮 How to Use

### ▶️ Graphical (humans → Stockfish)

```bash
python scripts/play_graphic.py
```

- Play by clicking.
- Human moves are fetched from Lichess.
- When you're off-book, Stockfish takes over.

---

### 🎤 Vocal Blindfold Mode

```bash
python scripts/play_vocal.py
```

- Play Stockfish **without visuals**, using your voice.
- Press **space**, speak your move ("Knight to f3", "e4", etc.)
- The board is updated and spoken aloud.

---

### 🧠 Tunable Stockfish Difficulty

```bash
python scripts/play_stockfish_tuned.py
```

- Adjust time/depth via keyboard:
  - `← / →` to tune time
  - `↑ / ↓` to tune depth
  - `T` to toggle between them

---

### 🧪 Tools

#### 🧙 Natural Language Move Translator

```bash
python tools/translate_move.py
```

Test how well natural commands like `"bishop to c4"` or `"e takes d4"` are understood.

#### 🔍 FEN Visualizer

```bash
python tools/view_fen.py
```

Paste in any FEN and view the position on a board.

---

## ✅ Example Commands Recognized

- `"Knight to f3"` → `g1f3`
- `"e takes d4"` → `e3d4`
- `"castle kingside"` → `e1g1`
- `"pawn to a4"` → `a2a4`
- `"bishop takes f6"` → `g5f6`

✔ All translated into valid UCI moves using current board state.

---

## 📦 Requirements

See `requirements.txt` for full list:

- `pygame`
- `python-chess`
- `speechrecognition`
- `pyttsx3`
- `cairosvg`
- `requests`

---

## 🚀 Future Plans

- 🔗 Merge vocal and human move logic into a single experience
- 🎙️ Natural voice command parsing (e.g. "play pawn to center")
- ⚙️ Adjustable difficulty & multiple engines (Leela, Torch, etc.)
- 🌐 Online play via Lichess or Chess.com automation
- 📈 Export to PGN, analyze with engine
- ↩️ Takebacks, manual move input, full training mode

---

## 👨‍💻 Author

Built with love by [Paul Lemaire](https://www.linkedin.com/in/paul-lemaire-aa0369289)

This is a hobby project — feel free to fork, explore, and contribute!  


## 🧪 Disclaimer

This is a personal side project made for fun and learning. Contributions and ideas welcome!

---

## 📄 License

MIT License – see `LICENSE` file.
