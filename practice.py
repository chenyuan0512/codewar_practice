class LineSafari:
    def __init__(self, grid):
        self.grid = grid
        self.direction = (0, 1)  # y, x 格式和 _find_X 一樣
        self.CORNER = "+"
        self.HOR = "-"
        self.VER = "|"

        self.valid_horizontal = {self.HOR, self.CORNER, "X"}  # 記得 X 也是合法的連接點
        self.valid_vertical = {self.VER, self.CORNER, "X"}
        self.start_point = (0, 0)

        # 先確認不會超過邊界
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.seen_x_times = 0
        self.previous_sign = " "

    # 這邊只要先找到第一個就好，因為不管從哪一個開始都會走到下一個

    def _find_X(self):
        for i in range(len(self.grid)):
            if "X" in self.grid[i]:
                self.y, self.x = i, self.grid[i].index("X")
                self.start_point = (self.y, self.x)
                self.previous_sign = "X"
                return # 如果沒有 return，會繼續找下一個

    def _find_lines_around(self):
        # self.y, self.x = pos[0], pos[1]
        y_up = self.y if self.y == 0 else self.y - 1
        y_down = self.y if self.y == len(self.grid) else self.y + 1

        x_left = self.x if self.x == 0 else self.x - 1
        x_right = self.x if self.x == len(self.grid) else self.x + 1
        print(y_up, y_down, x_left, x_right)
        print("center:", self.y, self.x)
        neighbor_list = [self._get_char(y_up, self.x), self._get_char(y_down, self.x), self._get_char(self.y, x_left), self._get_char(self.y, x_right)]
        print("neighbor list:", neighbor_list)
        # [上、下、左、右]

        return neighbor_list
    
    def _is_valid(self, r, c):
        return 0 <= r < self.height and 0 <= c < self.width

    def _get_char(self, r, c):
        if self._is_valid(r, c):
            return self.grid[r][c]

    def _walk_around(self):
        
        # 1. 找 X 位置: 只要第一次找完0就好
        # 這個應該從外面傳進來

        # 2. 找邊界: 先定義出上下、左右 index，這邊把 x 和 y 分開，統一先走 y
        next_round = self._find_lines_around()

        # 3. 找周圍: 看上下左右有沒有 symbol
        recurred_list = []

        for i in range(len(next_round)): # 因為在 self._find_lines_around 已經檢查過了，所以這邊不用再檢查一次
            y, x = 0, 0
            next = next_round[i]
            
            if next == " ":
                continue
            elif next == "X" and (self.y, self.x) == self.start_point:
                self.seen_x_times += 1
                continue

            elif i < 2:  
                if next == "-":
                    return "Fail"
                else:
                    y = -1 if i == 0 else 1
                    x = 0
            elif 1 < i:
                if next == "|":
                    return "Fail"
                else:
                    print(next)
                    x = -1 if i == 2 else 1
                    y = 0

            self.direction = (y, x)
            self.y += self.direction[0]
            self.x += self.direction[1]
            
            return "Ok"

        #     if next in self.valid_vertical and i < 2 and (self.y, self.x) != self.start_point:
        #         y = -1 if i == 0 else 1
        #         x = 0
        #         recurred_list.append(next)
        #         self.direction = [y, x]
        #     elif next in self.valid_horizontal and 1 < i and (self.y, self.x) != self.start_point:
        #         x = -1 if i == 2 else 1
        #         y = 0
        #         recurred_list.append(next)
        #         self.direction = [y, x]

        # # 這邊要 return 的應該是 list + 座標

        # self.y += self.direction[0]
        # self.x += self.direction[1]

        # return recurred_list

    
        # return None

    def run(self):
        self._find_X()

        result = self._walk_around()
        
        while self.seen_x_times < 2 and result == 'Ok':
            result = self._walk_around()

        # while "X" not in neighbor_list:
        #     neighbor_list = self._walk_around()
        #     print(neighbor_list)

        # 先檢查四周有幾條線


def line(grid):

    line = LineSafari(grid)
    # print(line.height, line.width)
    print(line.run())


grid = [
    "   |--------+    ",
    "X---        ---+ ",
    "               | ",
    "               X "
]
line(grid)
