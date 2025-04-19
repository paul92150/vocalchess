# ♟️ VocalChess – Play Blindfolded, With Your Voice

**VocalChess** is a fun personal project that explores how to play chess **blindfolded**, using only **your voice** to make moves.

Right now, two modes exist:
- A **vocal mode**, where you play against **Stockfish** using speech recognition and text-to-speech.
- A **graphical mode**, where you play against the most common **human moves** (scraped from Lichess) until the position is no longer known, then Stockfish takes over.

In the future, the goal is to **merge these two** so that you can speak your moves and face real human openings, fully blindfolded.

This is still a **work in progress**, but the core mechanics are working and ready to grow!


---

## 🎯 Goals

- 🔊 Play chess **without seeing the board**, using **speech recognition**.
- 🧠 Openings are based on **real human games** via the **Lichess Explorer API**.
- ♟️ When no human data is found for the current position, fallback to **Stockfish**.
- 🗣️ All moves (player and engine) are spoken out loud via **text-to-speech**.
- 🪄 Plan to support **natural language** like "knight takes e5" or "castle kingside".

---

## 🗂️ Project Structure

```
vocalchess/
├── assets/
│   └── pieces/             ← SVG pieces used for graphical version
├── scripts/
│   ├── play_graphic.py     ← Run the graphical version (see board, click)
│   └── play_vocal.py       ← Run the blindfold vocal version (speech only)
├── src/
│   ├── game/
│   │   ├── lichess_moves.py       ← Web scraping & move selection from Lichess
│   │   ├── stockfish_engine.py    ← Interface with Stockfish
│   │   └── fen_presets.py         ← Store FENs like Halloween Gambit etc.
│   ├── voice/
│   │   ├── recognizer.py          ← Speech-to-text (Google Speech Recognition)
│   │   ├── tts.py                 ← Text-to-speech using pyttsx3
│   │   └── keyboard_listener.py  ← Wait for space bar press to listen
│   ├── ui/
│   │   └── board_display.py       ← Draw board, pieces, sidebar (Pygame)
│   └── utils/
│       └── move_utils.py          ← Validate & process UCI moves
├── requirements.txt        ← Python dependencies
└── README.md               ← This file
```

---

## ⚙️ Installation

### 1. Clone the repo
```bash
git clone https://github.com/paul92150/vocalchess.git
cd vocalchess
```

### 2. Create a virtual environment (optional but recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Optional: Make `code` available in terminal (for VS Code users)
In VS Code, press `Cmd+Shift+P` → type "Shell Command" → click  
**“Install 'code' command in PATH”**

---

## 🧠 How to Play

### ▶️ Graphical version (see board & pieces)

```bash
python scripts/play_graphic.py
```

You can play by clicking pieces. It fetches human moves from Lichess and falls back to Stockfish.

---

### 🎤 Vocal Blindfold version

```bash
python scripts/play_vocal.py
```

- You **do not see** the board.
- Press `space` and **say your move aloud** (e.g., `"e2 to e4"` or `"knight f3"`).
- If your move is valid, the engine replies via voice.

---

## 🧪 Supported Voice Commands

Right now the voice parser is simple and expects UCI format like:

- `"e2 to e4"` → `e2e4`
- `"g one to f three"` → `g1f3`
- `"free"` is interpreted as `"3"` (e.g., `h free` → `h3`)

➡️ A full natural language parser is **planned** (see roadmap below).

---

## 🧱 Dependencies

See `requirements.txt` – includes:

- `speechrecognition`  
- `pyttsx3`  
- `python-chess`  
- `pygame`  
- `cairosvg`  
- `requests`

Make sure **Stockfish** is installed and available at `/opt/homebrew/bin/stockfish`, or edit the path in `stockfish_engine.py`.

---

## 🔮 Planned Improvements

- 🎙️ Better voice parsing (e.g. `"castle kingside"` → `O-O`)
- 🤖 Let users choose engine strength (Stockfish depth/time)
- 🧠 Play against **Leela**, **TorchChess**, or other engines
- 🧩 Voice-to-notation translator (e.g., `"knight to center"` → best candidate)
- 📤 Export games to **PGN** for Lichess import
- ↩️ Take back moves, analyze positions
- 🌐 Maybe allow **playing on Lichess or Chess.com** via automation (tbd)

---

## 🤓 Author

👨‍💻 Developed by [Paul Lemaire](https://www.linkedin.com/in/paul-lemaire-aa0369289)

---

## 🧪 Disclaimer

This is a personal side project made for fun and learning. Contributions and ideas welcome!

---

## 📄 License

MIT License – see `LICENSE` file.
