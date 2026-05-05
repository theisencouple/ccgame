# ccgame

A top-down adventure game built by the computer club. This project is designed for students who are just starting to learn programming — the code is kept simple and easy to follow.

## What it does

- A 30×30 world you can explore with the arrow keys
- A minimap that scrolls with you
- Each area shows a graphic and a description the first time you visit
- A message log at the bottom tracks what you've seen

## How to run

Create and activate a virtual environment:

```
python -m venv .venv
```

On Mac/Linux:
```
source .venv/bin/activate
```

On Windows:
```
.venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Then run the game:

```
python main.py
```

## Project structure

| File | What it does |
|---|---|
| `main.py` | Starts the game and runs the main loop |
| `ui/ui.py` | Draws everything on screen |
| `ui/panel.py` | `Panel` and `MessagePanel` classes for UI boxes |
| `area.py` | Defines what an area is and how the map is organized |
| `starting_area.py` | Builds the starting 30×30 world |
| `character.py` | Tracks the player's position and handles movement |

## Controls

| Key | Action |
|---|---|
| Arrow keys | Move |
| Page Up / Page Down | Scroll the message log |
