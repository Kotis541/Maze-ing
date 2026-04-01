import random
import math

class MazeGenerator():
    def __init__(self, config: dict):
        self._width = config['WIDTH']
        self._height = config['HEIGHT']
        self._entry = config['ENTRY']
        self._exit = config['EXIT']
        self._perfect = config['PERFECT']
        self._output = config['OUTPUT_FILE']
        self._maze = self._maze_init()

    def _maze_init(self) -> list[list[list]]:
        maze: list[list[list]] = []
        for i in range(0, self._width):
            maze.append([])
            for j in range(0, self._height):
                maze[i].append([1, 1, 1, 1])
        return maze

    def _was_visited(self, width: int, height: int) -> bool:
        if self._width >= 9 and self._height >= 7:
            c_width = math.ceil(self._width / 2)
            c_height = math.ceil(self._height / 2)
            logo = [[c_width - 1, c_height]]
            if [width, height] in logo:
                return True
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

    def _break_walls(self, path: list[list]) -> None:
        x1 = path[-1][0]
        x2 = path[-2][0]
        y1 = path[-1][1]
        y2 = path[-2][1]
        if x1 != x2:
            if x1 > x2:
                self._maze[x1][y1][3] = 0
                self._maze[x2][y2][1] = 0
            else:
                self._maze[x1][y1][1] = 0
                self._maze[x2][y2][3] = 0
        elif y1 != y2:
            if y1 > y2:
                self._maze[x1][y1][0] = 0
                self._maze[x2][y2][2] = 0
            else:
                self._maze[x1][y1][2] = 0
                self._maze[x2][y2][0] = 0

    def generate_maze(self) -> list[list[list]]:
        path = [self._entry]
        while path:
            cells = self._get_unvisited_cells(path[-1][0], path[-1][1])
            if not cells:
                path.pop()
            else:
                path.append(random.choice(cells))
                self._break_walls(path)
        with open(self._output, "w") as f:
            for y in range(0, self._height):
                for x in range(0, self._width):
                    z = self._maze[x][y][3] * 8 + self._maze[x][y][2] * 4
                    z += self._maze[x][y][1] * 2 + self._maze[x][y][0] * 1
                    f.write(f"{z:X}")
                f.write("\n")
            f.write(f"\n{str(self._entry)[1:-1]}\n{str(self._exit)[1:-1]}\n")
        return self._maze


########  TESTING  ############


# config je output co ti da parser
# config je treba na vytvoreni maze objektu
# obejkt.generate_maze() ti vrati 3D list s 1 0 