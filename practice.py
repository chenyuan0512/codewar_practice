class Dinglemouse(object):
    def __init__(self, queues, capacity):
        self.queues = queues  # queues 是所有樓層所有人要去哪一層的 info
        self.capacity = capacity  # 電梯最多可以載幾個人
        self.current_floor = 0  # 目前樓層
        self.lifted_passengers_list = []
        

        self.visited_list = [self.current_floor]
        self.direction = 1

    # 先把 queue 從 tuple 轉 list
    # 因為 tuple 是固定值，不能更動

    def _tuple_to_index(self):
        self.queues_list = [list(i) for i in self.queues]
        # self.queues_list_copy = self.queues_list.copy()

    # 出去
    def _leave(self):
        self.lifted_passengers_list = [
            p for p in self.lifted_passengers_list if p != self.current_floor]
        self._record_visited_floor()

    # 紀錄目前樓層
    def _record_visited_floor(self):
        if self.current_floor != self.visited_list[-1]:
            self.visited_list.append(self.current_floor)

    def _next_floor(self):
        while True:
            print(self.visited_list)
            empty = 0
            for i in self.queues_list:
                if i == []:
                    empty += 1
                if empty == len(self.queues_list) and self.lifted_passengers_list == []:
                    self.current_floor = 0
                    self._record_visited_floor()
                    return self.visited_list

            # 現在改成每個樓層都停下來檢查

            # 檢查有沒有人要出去
            if self.current_floor in self.lifted_passengers_list:
                self._leave()

            # 檢查有沒有人要進來
            for target_floor in list(self.queues_list[self.current_floor]):
                if (self.direction > 0 and target_floor > self.current_floor) or (self.direction < 0 and target_floor < self.current_floor):
                    if len(self.lifted_passengers_list) < self.capacity:
                        self.lifted_passengers_list.append(target_floor)
                        self.queues_list[self.current_floor].remove(target_floor)
                    self._record_visited_floor()
            

            self.current_floor += self.direction

            if self.current_floor >= len(self.queues_list) - 1:
                self.current_floor = len(self.queues_list) - 1
                self.direction = -1

            elif self.current_floor <= 0:
                self.current_floor = 0
                self.direction = 1


    def theLift(self):
        self._tuple_to_index()
        visited = self._next_floor()
        # print("current floor", self.current_floor)
        # print("target_floor: ", self.target_floor_list)
        # print("number_inside_elevator: ", self.lift_passengers_list)
        print("visited: ", visited)

        # print(self.queues)
        # self._next_floor()
        return visited


# Floors:    G     1      2        3     4      5      6         Answers:
tests = [
    # [((),   (),    (5, 5, 5), (),   (),    (),    ()),     [0, 2, 5, 0]],
    # [((),   (),    (1, 1),   (),   (),    (),    ()),     [0, 2, 1, 0]],
    # [((),   (3,),  (4,),    (),   (5,),  (),    ()),     [0, 1, 2, 3, 4, 5, 0]],
    [((),   (0,),  (),      (),   (2,),  (3,),  ()),     [0, 5, 4, 3, 2, 1, 0]],
    # [((),   (6, 6, 6, 5, 0, 0, 0, 0, 0, 0,),  (),  (),   (),
    #   (1, 1, 1, 1, 0, ),  (5,)),     [0, 5, 4, 3, 2, 1, 0]]
]

for queues, answer in tests:
    # print(queues)
    lift = Dinglemouse(queues, 5)
    lift.theLift()
