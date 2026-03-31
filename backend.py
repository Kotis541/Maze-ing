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
        for i in range(0, self._height):
            maze.append([])
            for j in range(0, self._width):
                maze[i].append([1, 1, 1, 1])
        return maze

    def _was_visited(self, height: int, width: int) -> bool:
        return 0 in self._maze[height][width]
