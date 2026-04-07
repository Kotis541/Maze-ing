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
        if 'SEED' in config:
            random.seed(config['SEED'])
        if self._width >= 9 and self._height >= 7:
            self._logo = self._logo_init()
            if (list(self._entry) in self._logo
                    or list(self._exit) in self._logo):
                x = "ENTRY or EXIT coordinates clash with 42 logo, try again"
                print(x)
                raise ValueError(x)
        else:
            self._logo = []

    def _maze_init(self) -> list[list[list]]:
        maze: list[list[list]] = []
        for i in range(0, self._width):
            maze.append([])
            for j in range(0, self._height):
                maze[i].append([1, 1, 1, 1])
        return maze

    def _logo_init(self) -> list[list[int]]:
        c_width = math.ceil(self._width / 2)
        c_height = math.ceil(self._height / 2)
        logo = [
            [c_width - 2, c_height], [c_width - 3, c_height],
            [c_width - 4, c_height], [c_width - 4, c_height - 1],
            [c_width - 4, c_height - 2], [c_width - 2, c_height + 1],
            [c_width - 2, c_height + 2], [c_width, c_height],
            [c_width, c_height + 1], [c_width, c_height + 2],
            [c_width + 1, c_height + 2], [c_width + 2, c_height + 2],
            [c_width, c_height], [c_width + 1, c_height],
            [c_width + 2, c_height], [c_width + 2, c_height - 1],
            [c_width + 2, c_height - 2], [c_width + 1, c_height - 2],
            [c_width, c_height - 2]
        ]
        return logo

    def _was_visited(self, width: int, height: int) -> bool:
        if [width, height] in self._logo:
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

    def _gen_coord(self) -> list[int, int]:
        while 1:
            x = random.randrange(self._width)
            y = random.randrange(self._height)
            if [x, y] not in self._logo:
                return [x, y]

    def _non_logo(self, coord: list[int, int]) -> list[list]:
        res = []
        x = coord[0]
        y = coord[1]
        if x - 1 >= 0:
            if [x - 1, y] not in self._logo:
                res.append([x - 1, y])
        if x + 1 < self._width:
            if [x + 1, y] not in self._logo:
                res.append([x + 1, y])
        if y + 1 < self._height:
            if [x, y + 1] not in self._logo:
                res.append([x, y + 1])
        if y - 1 >= 0:
            if [x, y - 1] not in self._logo:
                res.append([x, y - 1])
        return res

    def generate_maze(self) -> list[list[list]]:
        path = [self._entry]
        while path:
            cells = self._get_unvisited_cells(path[-1][0], path[-1][1])
            if not cells:
                path.pop()
            else:
                path.append(random.choice(cells))
                self._break_walls(path)
        if not self._perfect:
            walls_down = round(self._width * self._height * 0.25)
            for i in range(0, walls_down):
                coord = self._gen_coord()
                cells = self._non_logo(coord)
                if cells:
                    self._break_walls([coord, random.choice(cells)])
        with open(self._output, "w") as f:
            for y in range(0, self._height):
                for x in range(0, self._width):
                    z = self._maze[x][y][3] * 8 + self._maze[x][y][2] * 4
                    z += self._maze[x][y][1] * 2 + self._maze[x][y][0] * 1
                    f.write(f"{z:X}")
                f.write("\n")
            f.write(f"\n{str(self._entry)[1:-1]}\n{str(self._exit)[1:-1]}\n")
        return self._maze

    def _calc_h(self, coord1: tuple[int, int]) -> int:
        return abs(coord1[0] - self._exit[0]) + abs(coord1[1] - self._exit[1])

    def _calc_f(self, new_g: int, coord: tuple[int, int]) -> int:
        return self._calc_h(coord) + new_g

    def _valid_cells(self, x: int, y: int) -> list[list[int]]:
        res: list[list[int]] = []
        if self._maze[x][y][0] == 0:
            res.append([x, y - 1])
        if self._maze[x][y][1] == 0:
            res.append([x + 1, y])
        if self._maze[x][y][2] == 0:
            res.append([x, y + 1])
        if self._maze[x][y][3] == 0:
            res.append([x - 1, y])
        return res

    def _push_direction(self, coord1: list, coord2: list) -> str:
        if coord1[0] != coord2[0]:
            if coord1[0] > coord2[0]:
                return "W"
            else:
                return "E"
        elif coord1[1] != coord2[1]:
            if coord1[1] > coord2[1]:
                return "N"
            else:
                return "S"

    def find_path(self) -> list[list[int]]:
        entry_tuple = tuple(self._entry)
        exit_tuple = tuple(self._exit)
        open_set = {
            entry_tuple: {
                'parent': None, 'g': 0, 'f': self._calc_h(entry_tuple)
                }
            }
        closed_set = {}
        while exit_tuple not in closed_set:
            lowest_f = float('inf')
            current = None
            for coord, data in open_set.items():
                if data['f'] < lowest_f:
                    current = coord
                    lowest_f = data['f']
            temp_list = self._valid_cells(current[0], current[1])
            for elem in temp_list:
                x = tuple(elem)
                if x not in closed_set:
                    new_g = open_set[current]['g'] + 1
                    if x in open_set and open_set[x]['g'] <= new_g:
                        continue
                    else:
                        f = self._calc_f(new_g, x)
                        open_set[x] = {'parent': current, 'g': new_g, 'f': f}
            closed_set[current] = open_set.pop(current)
        final_path = [list(exit_tuple)]
        x = closed_set[exit_tuple]['parent']
        output = self._push_direction(list(x), list(exit_tuple))
        while x:
            final_path.insert(0, list(x))
            temp = list(x)
            x = closed_set[x]['parent']
            if x:
                output = self._push_direction(list(x), temp) + output
        with open(self._output, "a") as f:
            f.write(f"{output}\n")
        return final_path
