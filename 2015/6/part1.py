def init_grid() -> list[list[int]]:
    return [[0 for _ in range(1000)] for _ in range(1000)]


class LightController:
    def __init__(self, matrix: list[list[int]]):
        self._matrix = matrix

    def lit_lights(self) -> int:
        n = 0
        for row in self._matrix:
            for col in row:
                if col == 1:
                    n += 1
        return n

    def _turn_on(self, start, end):
        for i in range(start[0], end[0]+1):
            for j in range(start[1], end[1]+1):
                self._matrix[i][j] = 1

    def _turn_off(self, start, end):
        for i in range(start[0], end[0]+1):
            for j in range(start[1], end[1]+1):
                self._matrix[i][j] = 0

    def _toggle(self, start, end):
        for i in range(start[0], end[0]+1):
            for j in range(start[1], end[1]+1):
                value = self._matrix[i][j]
                if value == 0:
                    self._matrix[i][j] = 1
                else:
                    self._matrix[i][j] = 0

    def process_command(self, cmd: list[str]):
        start = list(map(lambda x: int(x), cmd[-3].split(",")))
        end = list(map(lambda x: int(x), cmd[-1].split(",")))
        match f"{cmd[0]} {cmd[1]}":
            case "turn on":
                self._turn_on(start, end)
            case "turn off":
                self._turn_off(start, end)
            case _:
                self._toggle(start, end)


matrix = init_grid()
controller = LightController(matrix)

with open("input.txt", "r") as f:
    for command in f.readlines():
        controller.process_command(command.split())

print(controller.lit_lights())
