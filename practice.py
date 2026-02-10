class LineSafari:
    def __init__(self, grid):
        self.grid = grid
        self.direction = [0, 1]  # y, x 格式和 _find_X 一樣
        self.CORNER = "+"
        self.HOR = "-"
        self.VER = "|"

        self.valid_horizontal = {self.HOR, self.CORNER, "X"}  # 記得 X 也是合法的連接點
        self.valid_vertical = {self.VER, self.CORNER, "X"}
        self.start_point = (0, 0)

        # 先確認不會超過邊界
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    # 這邊只要先找到第一個就好，因為不管從哪一個開始都會走到下一個

    def _find_X(self):
        for i in range(len(self.grid)):
            if "X" in self.grid[i]:
                self.y, self.x = i, self.grid[i].index("X")
                self.start_point = (self.y, self.x)
                # return [i, self.grid[i].index("X")]

    def _find_lines_around(self):
        # self.y, self.x = pos[0], pos[1]
        y_up = self.y if self.y == 0 else self.y - 1
        y_down = self.y if self.y == len(self.grid) else self.y + 1

        x_left = self.x if self.x == 0 else self.x - 1
        x_right = self.x if self.x == len(self.grid) else self.x + 1

        neighbor_list = [self._get_char(y_up, self.x), self._get_char(
            y_down, self.x), self._get_char(self.y, x_left), self._get_char(self.y, x_right)]
        # [上、下、左、右]

        return neighbor_list

    def _walk_around(self):
        # 1. 找 X 位置: 只要第一次找完0就好
        # 這個應該從外面傳進來

        # 2. 找邊界: 先定義出上下左右 index
        next_round = self._find_lines_around()

        # 3. 找周圍: 看上下左右有沒有 symbol
        recurred_list = []

        for i in range(len(next_round)):
            next = self._get_char()
            if next_round[i] in self.valid_vertical and i < 2 and (self.y, self.x) != self.start_point:
                valid = next_round[i]
                y = -1 if i == 0 else 1
                x = 0
                recurred_list.append(valid)
                self.direction = [y, x]

            elif next_round[i] in self.valid_horizontal and 1 < i and (self.y, self.x) != self.start_point:
                valid = next_round[i]
                x = -1 if i == 2 else 1
                y = 0
                recurred_list.append(valid)
                self.direction = [y, x]

        # 這邊要 return 的應該是 list + 座標

        self.y += self.direction[0]
        self.x += self.direction[1]

        return recurred_list

    def _is_valid(self, r, c):
        return 0 <= r < self.height and 0 <= c < self.width

    def _get_char(self, r, c):
        if self.is_valid(r, c):
            return self.grid[r][c]
        return None

    def run(self):
        self._find_X()
        neighbor_list = self._walk_around()

        while "X" not in neighbor_list:
            neighbor_list = self._walk_around()
            print(neighbor_list)

        # 先檢查四周有幾條線


def line(grid):

    line = LineSafari(grid)
    print(line.height, line.width)
    # print(line.run())


grid = [
    "   |--------+    ",
    "X---        ---+ ",
    "               | ",
    "               X "
]
line(grid)
