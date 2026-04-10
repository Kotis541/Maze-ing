#!/usr/bin/env python3

from parser import read_config
from maze_gen import MazeGenerator
from typing import Any
import math

N = 0  # sever
E = 1  # vychod
S = 2  # jih
W = 3  # zapad

RESET = "\033[0m"
LOGO = "\033[42m"
PATH = "\033[40m"
ENTRY = "\033[44m"
EXIT = "\033[41m"
WALL = "\033[42m"
PATH_COLOR = "\033[46m"


def get_logo_cells(width: int, height: int) -> set[tuple[int, int]]:
    """
    Returns a set of (x, y) coordinates representing the cells
    that form a logo in the center of the maze.
    """

    if width < 9 or height < 7:
        return set()

    c_width = math.ceil(width / 2)
    c_height = math.ceil(height / 2)

    logo = [
        (c_width - 2, c_height), (c_width - 3, c_height),
        (c_width - 4, c_height), (c_width - 4, c_height - 1),
        (c_width - 4, c_height - 2), (c_width - 2, c_height + 1),
        (c_width - 2, c_height + 2), (c_width, c_height),
        (c_width, c_height + 1), (c_width, c_height + 2),
        (c_width + 1, c_height + 2), (c_width + 2, c_height + 2),
        (c_width + 1, c_height), (c_width + 2, c_height),
        (c_width + 2, c_height - 1), (c_width + 2, c_height - 2),
        (c_width + 1, c_height - 2), (c_width, c_height - 2)
    ]
    return set(logo)


def render_maze(maze: list[list[list[int]]], entry: tuple, exit: tuple,
                wall_color=WALL, path=None, path_color=None) -> None:
    """Renders the maze in the terminal using colored output."""

    width = len(maze)
    height = len(maze[0]) if width else 0
    WALL = wall_color
    LOGO = wall_color
    path_position = set()
    if path:
        for i in range(len(path)):
            x, y = path[i]
            path_position.add((x * 2 + 1, y * 2 + 1))
            if i == 0:
                continue
            px, py = path[i - 1]
            mx = x + px
            my = y + py
            path_position.add((mx + 1, my + 1))

    grid_h = height * 2 + 1
    grid_w = width * 2 + 1
    grid = [[1 for _ in range(grid_w)] for _ in range(grid_h)]
    logo_cells = get_logo_cells(width, height)
    logo_position = {(x * 2 + 1, y * 2 + 1) for (x, y) in logo_cells}

    for y in range(height):
        for x in range(width):
            cell = maze[x][y]
            cy = y * 2 + 1
            cx = x * 2 + 1
            grid[cy][cx] = 0

            if cell[N] == 0:
                grid[cy - 1][cx] = 0
            if cell[S] == 0:
                grid[cy + 1][cx] = 0
            if cell[W] == 0:
                grid[cy][cx - 1] = 0
            if cell[E] == 0:
                grid[cy][cx + 1] = 0

    entry_pos = (entry[0] * 2 + 1, entry[1] * 2 + 1)
    exit_pos = (exit[0] * 2 + 1, exit[1] * 2 + 1)

    for gy in range(grid_h):
        for gx in range(grid_w):
            if (gx, gy) == entry_pos:
                print(f"{ENTRY}  {RESET}", end="")
            elif (gx, gy) == exit_pos:
                print(f"{EXIT}  {RESET}", end="")
            elif (gx, gy) in logo_position:
                print(f"{LOGO}  {RESET}", end="")
            elif (gx, gy) in path_position:
                print(f"{path_color}  {RESET}", end="")
            elif grid[gy][gx] == 1:
                print(f"{WALL}  {RESET}", end="")
            else:
                print(f"{PATH}  {RESET}", end="")
        print()


def change_color(reverse: bool = False):
    """Cycles through a predefined list of ANSI color codes."""

    colors = [
        "\033[47m",
        "\033[43m",
        "\033[45m",
        "\033[46m",
        "\033[42m"
    ]
    idx = len(colors) - 1 if reverse else 0
    step = -1 if reverse else 1

    while 1:
        yield colors[idx]
        idx = (idx + step) % len(colors)


def load_config() -> dict[Any, Any]:
    """Loads the maze configuration from an external source."""
    config = read_config()
    if config is None:
        exit()
    return config


def main() -> None:
    """The main entry point for the maze game."""
    config = load_config()
    color_cycle = change_color(reverse=True)
    wall_color = next(color_cycle)
    path_display_color = next(color_cycle)

    try:
        maze = MazeGenerator(config)
    except Exception as e:
        print(e)
        exit()

    genereted_list = maze.generate_maze()
    path = maze.find_path()
    show_path = False
    render_maze(genereted_list,
                config['ENTRY'],
                config['EXIT'],
                path=path if show_path else None,
                path_color=path_display_color)

    while True:
        print()
        print("=== A-Maze-ing ===")
        print("1. Re-generate a new maze")
        print("2. Show/Hide path from entry to exit")
        print("3. Rotate maze colors")
        print("4. Quit")

        try:
            user_input = int(input("Choice? (1 - 4): "))
        except ValueError:
            print("[ERROR] - Please choose between 1 - 4!")
            continue
        except KeyboardInterrupt:
            print("\nThanks for playing our game!")
            break

        if user_input == 1:
            config = load_config()
            try:
                maze = MazeGenerator(config)
                genereted_list = maze.generate_maze()
                path = maze.find_path()
                show_path = False
                render_maze(genereted_list,
                            config['ENTRY'],
                            config['EXIT'],
                            wall_color,
                            path=path if show_path else None,
                            path_color=path_display_color)
            except TypeError:
                exit()

        elif user_input == 2:
            show_path = not show_path
            render_maze(genereted_list,
                        config['ENTRY'],
                        config["EXIT"],
                        wall_color,
                        path=path if show_path else None,
                        path_color=path_display_color)

        elif user_input == 3:
            path_display_color = wall_color
            wall_color = next(color_cycle)
            render_maze(genereted_list,
                        config['ENTRY'],
                        config["EXIT"],
                        wall_color,
                        path=path if show_path else None,
                        path_color=path_display_color)

        elif user_input == 4:
            break

        else:
            print("[ERROR] - Please choose between 1 - 4")


if __name__ == "__main__":
    main()
