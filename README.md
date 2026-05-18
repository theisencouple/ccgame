# ccgame

A top-down adventure game built by the computer club. Walk around a world map, discover new areas, and explore a village full of streets, houses, and a blacksmith.

## What it does

- Explore a 30×30 world using the arrow keys
- Enter the village and walk around its streets, houses, and blacksmith
- Press **E** to travel between the world map and the village
- A minimap in the corner shows the surrounding area
- The first time you visit a new tile, you get a description of it
- A message log at the bottom keeps track of everywhere you've been

## How to run it

### Step 1 — Set up a virtual environment

A virtual environment is a private folder where Python keeps the packages this project needs, separate from everything else on your computer.

On Mac or Linux:
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
| E | Enter or exit a location |
| Page Up / Page Down | Scroll the message log |

## How to run the tests

```
pytest
```

## How the code is organized

The project is split into folders so that related code lives together.

### Top-level files

| File | What it does |
|---|---|
| `main.py` | Where the game starts. Sets up the window, places the player on the village tile, and runs the game loop at 30 FPS — checking for key presses and redrawing the screen every frame. |
| `character.py` | Tracks where the player is and what map they're on. Handles arrow key movement, the E key for entering and exiting locations, and draws the available controls at the bottom of the screen. |

### The `areas/` folder — one file per tile type

Every place in the game is an "area" — a tile with a name, a short description (shown on first visit), a color on the minimap, and an optional image shown in the side panel. Each file below defines one type of tile.

| File | What it does |
|---|---|
| `areas/base.py` | The template every tile is built from. Defines the name, description, color, and image. Also handles dimming unvisited tiles on the minimap (darker until you've been there). |
| `areas/field.py` | A grassy field — the default tile that covers most of the world. |
| `areas/forest.py` | A dense forest in the northwest corner of the map. |
| `areas/cave.py` | A cluster of dark caves to the east of center. |
| `areas/lake.py` | A calm lake in the southeast corner. |
| `areas/strawberry_field.py` | Wild strawberry fields south of center. |
| `areas/village.py` | The village tile on the world map — where the player starts. Press **E** here to enter the village. |
| `areas/village_street.py` | A dusty dirt road inside the village. |
| `areas/village_house.py` | A modest home with a thatched roof. |
| `areas/blacksmith.py` | A forge where the hammering never stops. |
| `areas/village_gate.py` | The village gate — press **E** here to return to the world map. |

### The `sections/` folder — one file per map

A "section" is a full map — a grid of tiles the player can walk around. The game has two sections: the big world map and the village.

| File | What it does |
|---|---|
| `sections/base.py` | Defines what a section is: a 2D grid of tiles with methods to move the player north, south, east, or west. Also defines the `Enterable` and `Exitable` labels used to mark tiles that can teleport the player to another map when E is pressed. Includes a `find()` helper that searches the grid for a specific tile and returns its position. |
| `sections/starting_area.py` | Builds the 30×30 world map. Places forests in the northwest, a lake in the southeast, caves to the east, strawberry fields to the south, and the village at the center. Also connects the two maps together: stepping on the village tile takes you to the village map at the gate, and stepping on the gate takes you back to the village tile. |
| `sections/village_section.py` | Builds the village map — a 5×4 grid of streets, houses, a blacksmith, and a gate. The gate tile sits at the bottom-center and is where the player arrives and departs. |

### The `ui/` folder — everything drawn on screen

| File | What it does |
|---|---|
| `ui/colors.py` | A list of colors (as red, green, blue numbers) used throughout the game — one for each tile type and one for each UI element. |
| `ui/base.py` | Low-level drawing tools: how to draw text, filled rectangles, and images using Pygame. Also handles loading and caching image files, and word-wrapping long text to fit inside a panel. |
| `ui/panel.py` | Defines the three kinds of panels drawn on screen: a plain box, a box with a title, and a scrollable message log. Areas display their name and image in a panel; the message log collects all first-visit descriptions. |
| `ui/ui.py` | Puts all the panels together into a single 1100×700 window. Defines the layout: minimap on the left, controls below it, area detail panel top-right, message log bottom-right. |
