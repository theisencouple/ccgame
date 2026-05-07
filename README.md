# ccgame

A top-down adventure game built by the computer club. You can walk around a map, discover new areas, and read about what you find.

## What it does

- Explore a 30×30 world using the arrow keys
- A small map in the corner shows where you are
- The first time you visit a new place, you get a description and a picture of it
- A message log at the bottom keeps track of everywhere you've been

## How to run it

### Step 1 — Set up a virtual environment

A virtual environment is a private folder where Python keeps the packages this project needs, separate from everything else on your computer.

On Mac or Linux, open a terminal in this folder and run:
```
python -m venv .venv
source .venv/bin/activate
```

On Windows:
```
python -m venv .venv
.venv\Scripts\activate
```

You'll know it worked when you see `(.venv)` at the start of your terminal prompt.

### Step 2 — Install the packages

This game uses a package called `pygame` that handles the window, graphics, and keyboard input. Install it by running:

```
pip install -r requirements.txt
```

### Step 3 — Run the game

```
python main.py
```

## Controls

| Key | Action |
|---|---|
| Arrow keys | Move around |
| Page Up / Page Down | Scroll the message log |

## How to run the tests

Tests are small programs that check whether the code is working correctly. Run them with:

```
pytest
```

## How the code is organized

The project is split into folders so that related code lives together.

**The main files:**

| File | What it does |
|---|---|
| `main.py` | This is where the game starts. It sets up the window and runs the game loop — the loop that keeps the game running and checks for key presses. |
| `character.py` | Keeps track of where the player is on the map and moves them when an arrow key is pressed. |

**The `areas/` folder** — everything about the world:

| File | What it does |
|---|---|
| `areas/base.py` | Defines what an "area" is: a tile on the map with a name, a color, a description, and an optional picture. |
| `areas/starting_area.py` | Builds the actual 30×30 map by placing terrain types in different spots. |
| `areas/field.py` | A grassy field. |
| `areas/forest.py` | A dense forest. |
| `areas/cave.py` | A dark cave. |
| `areas/lake.py` | A calm lake. |
| `areas/village.py` | A small village — this is where you start. |
| `areas/strawberry_field.py` | A field of wild strawberries. |

**The `ui/` folder** — everything about drawing to the screen:

| File | What it does |
|---|---|
| `ui/colors.py` | A list of colors used throughout the game, like the color of each terrain type. |
| `ui/base.py` | Low-level drawing tools: how to draw text, rectangles, and images using pygame. |
| `ui/panel.py` | A "panel" is one of the boxes you see on screen. This file defines how panels are drawn and how the message log works. |
| `ui/ui.py` | Puts all the panels together and defines the layout of the full game window. |