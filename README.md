<i>This project has been created as part
of the 42 curriculum by vokotera and pzavada<i>

<h1>Description</h1>
A-maze-ing is a Python maze generator and visualizer. The program reads a configuration file, generates a valid maze with embed 42 pattern in the center. After that it writes the result into the output file using hexadecimal wall encoding.

<h1> Instructions </h1>

<h3>Installation</h3>
<pre>make install </pre>
This install all project dependencies via pip

<h3>Running program</h3>
<pre>make run</pre>
or
<pre>./a-maze-ing.py config.txt</pre>

**Debug mode**
<pre>make debug</pre>

<h3>Linting</h3>
<pre>make lint</pre>

<h3>Cleanup</h3>
<pre>make clean</pre>

---

**Configuration File**

The configuration file uses `KEY=VALUE` pairs (one per line). Lines starting with `#` are comments and are ignored - barring the `SEED` all pairs are required.

| Key           | Description                          | Example                  
|---------------|--------------------------------------|--------------------------
| `WIDTH`       | Maze width (number of cells)         | `WIDTH=20`               |
| `HEIGHT`      | Maze height (number of cells)        | `HEIGHT=15`              |
| `ENTRY`       | Entry cell coordinates (x,y)         | `ENTRY=0,0`              |
| `EXIT`        | Exit cell coordinates (x,y)          | `EXIT=19,14`             |
| `OUTPUT_FILE` | Path to the output file              | `OUTPUT_FILE=maze.txt`   |
| `PERFECT`     | Generate a perfect maze (True/False) | `PERFECT=True`           |
| `SEED`        | Random seed for reproducibility      | `SEED=42`                |


**Example `config.txt`:**
```ini
WIDTH=20
HEIGHT=15
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=True
SEED=42
```
<h1>Team & Project Management</h1>

## Maze generation algorithm
For our maze generation, we implemented the Recursive Backtracking (Randomized Depth-First Search) algorithm. The process begins with a grid that is completely walled off and proceeds as follows starting from the entry coordinate:

- Randomly choose one unvisited neighboring cell.
- Step into that cell and break the connecting wall.
- If no neighboring cells are unvisited, backtrack along the path until an unvisited neighbor is found.
- Continue this process until all cells in the grid have been visited.

This algorithm inherently generates a "perfect" maze (meaning there is exactly one path between any two points and no loops). To allow for the creation of non-perfect mazes, we introduced a post-generation step:

- Randomly select a valid coordinate and break a wall connecting it to a non-logo neighbor.
- Repeat this process until an amount of walls equal to 25% of the total grid area has been removed, creating multiple potential paths.

### Why we chose this algorithm
We selected recursive backtracking because it is highly intuitive, straightforward to implement, and efficient. It reliably generates long, winding corridors that make for visually interesting and challenging unique mazes without requiring overly complex data structures.

### Code Reusability
The codebase is built using a modular Object-Oriented approach, making several components easily reusable for future projects:

- The MazeGenerator Class: Because the class is entirely driven by a config dictionary passed during initialization, you can drop this exact class into another Python project. You can generate completely different mazes just by feeding it a new dictionary with different dimensions, seeds, or entry/exit points.

- Decoupled Pathfinding: The A* pathfinding logic (find_path, _calc_h, _calc_f) is separated from the generation logic. It simply reads the existing _maze array. This means you could bypass the recursive backtracking entirely, load a pre-made maze from a file into the _maze array, and still reuse the A* algorithm to solve it.

- Grid Utilities: Helper methods like _get_unvisited_cells, _valid_cells, and the directional mapping (_push_direction) are generic enough to be ripped out and reused in other 2D grid-based games or alternative maze generation algorithms (like Prim's or Kruskal's).

## Reusing the Maze Generator Module

This project includes a standalone Python package (`.whl` and `.tar.gz`) that allows you to easily reuse the maze generation and pathfinding logic.

### Installation

Install the module locally using `pip` (a virtual environment is recommended):

```bash
# 1. Install build
pip install build

#2. Build the module
python -m build --wheel

# 3. Install the built wheel
pip install ./dist/mazegen-1.0.0-py3-none-any.whl

# 4. Now this works
pip show mazegen
```

### Usage example

You can import the MazeGenerator class, pass custom parameters via a dictionary, and directly access both the maze structure and the calculated solution.
```ini
from maze_gen import MazeGenerator

# 1. Define custom parameters
config = {
    'WIDTH': 25,
    'HEIGHT': 25,
    'ENTRY': (0, 0),
    'EXIT': (24, 24),
    'PERFECT': True,
    'OUTPUT_FILE': 'maze.txt',
    'SEED': 42
}

# 2. Instantiate the generator
generator = MazeGenerator(config)

# 3. Access the generated structure (returns a 3D list of cells and walls)
maze_grid = generator.generate_maze()

# 4. Access the solution (returns the A* path as a list of coordinates)
solution_path = generator.find_path()
```

## Roles
 - vokotera - Visual rendering, user interface, README file and Makefile
 - pzavada - Maze generation algorithm, ouput file, config parsing 

## Planning
We used AI to help us organize the project into 2 specific roles. This allowed us to:
 - Divide: Each of us took full responsibility for one part
 - Work Separately: We started working on our own section 
Like that we were able to work how we define until end

## What worked well
Team working worked very well and the algorithm that we chose to use.
We could improve maze rendering by using miniLBX or different colors next time.

## Specific tools?
- flake8, mypy for code quality
- Claude AI and gemini for brainstorming and helping with code

<h1>Resources</h1>

 - [Youtube - Maze algorithm](https://www.youtube.com/watch?is=g33h4t98knfFA5SB&v=jZQ31-4_8KM)
 - https://www.geeksforgeeks.org/ 

### AI usage
- AI tools were used during the development of this project to gain a deeper understanding of the core concepts and to assist with coding and debugging. No code was blindly copy-pasted without a full comprehension of its functionality