import random

class MazeGenerator():
    def __init__(self, config: dict):
        self._width = config['WIDTH']
        self._height = config['HEIGHT']
        self._entry = config['ENTRY']
        self._exit = config['EXIT']
        self._perfect = config['PERFECT']
        self._maze = self._maze_init()

    def _maze_init(self) -> list[list[list]]:
        maze = []
        for i in range(0, self._width):
            maze.append([])
            for j in range(0, self._height):
                maze[i].append([1, 1, 1, 1])
        return maze

    def _was_visited(self, height: int, width: int) -> bool:
        return 0 in self._maze[width][height]

    def _get_unvisited_cells(self, x, y) -> list[list]:
        res = []
        if y - 1 >= 0:
            if not self._was_visited(x, y - 1):
                res.append([x, y - 1])
        if y + 1 < self._height:
            if not self._was_visited(x, y + 1):
                res.append([x, y + 1])
        if x - 1 >= 0:
            if not self._was_visited(x - 1, y):
                res.append([x - 1, y])
        if x + 1 < self._width:
            if not self._was_visited(x + 1, y):
                res.append([x + 1, y])
        return res

    def generate_maze(self) -> list[list[list]]:
        path = [self._entry]
        while path:
            cells = self._get_unvisited_cells(path[-1][0], path[-1][1])
            if not cells:
                path.pop()
            else:
                print("x")



########  TESTING  ############
import sys
import os


def read_config() -> dict:
    res = {}
    if len(sys.argv) != 2:
        print("No valid configuration file, please try again!")
    elif os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as file:
            for line in file:
                if not line or line.startswith("#"):
                    continue
                if '=' in line:
                    key, value = line.strip().split("=")
                    res[key] = value
                else:
                    print("No valid configuration file, please try again!")
                    return None
            try:
                res['WIDTH'] = int(res['WIDTH'])
                res['HEIGHT'] = int(res['HEIGHT'])

                exit_err = res['ENTRY'].split(",")
                if len(exit_err) != 2:
                    raise ValueError(f"ENTRY: {exit_err}")
                else:
                    res['ENTRY'] = (int(exit_err[0]), int(exit_err[1]))

                exit_err = res['EXIT'].split(",")
                if len(exit_err) != 2:
                    raise ValueError(f"EXIT: {exit_err}")
                else:
                    res['EXIT'] = (int(exit_err[0]), int(exit_err[1]))

                bool_map = {"TRUE": True, "FALSE": False}
                res['PERFECT'] = bool_map[res['PERFECT'].upper()]
            except KeyError as e:
                print(
                    "Configuration Error: Missing or",
                    f"misspelled mandatory key {e}"
                    )
                return None
            except ValueError as e:
                print(f"Configuration Error: Invalid data format or value {e}")
                return None
            except Exception as e:
                print(f"An unxepected error occured: {e}")
                return None
        return res
    else:
        print("No valid configuration file, please try again!")



maze = MazeGenerator(read_config())
print(maze._get_unvisited_cells(12, 10))

                
