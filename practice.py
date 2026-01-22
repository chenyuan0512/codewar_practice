def find_word(board, word):

    states: list = []  # 目前所有候選，(pos, visited)
    # k: int = 1  # word index

    board_size = len(board)

    # 先找到第一個字母位置
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == word[0]:
                pos = (i, j)
                visited = {(i, j)}
                states.append((pos, visited))
                # state.append((i, j))
                # print(i, j)
                # print(neighbors(i, j))
    print(f"states: ", states)
    if len(states) == 0:
        return False

    # neighbor_list = neighbors(r, c, board)
    for k in range(1, len(word)):
        new_states: list = []  # 下一輪候選

        for i in range(len(states)):
            print(states)
            pos = states[i][0]
            visited = states[i][1]
            r, c = pos

            neighbor_list = neighbors(r, c, board)
            # print(f"r, c:", r, c)
            # print(f"pos = ", pos)
            # print(f"neighbor_list:", neighbor_list)

            for a in neighbor_list:
                # 第二個字母
                if a[0] == word[k] and (a[1], a[2]) not in visited:
                    visited2 = visited.copy()
                    neighbor_pos = (a[1], a[2])
                    visited2.add(neighbor_pos)
                    # print(f"visited2:", visited2)
                    # overlap_list.append((a[1], a[2]))
                    new_states.append(((a[1], a[2]), visited2))
            print(f"new_state:", new_states)
        if len(new_states) == 0:
            return False
        else:
            states = new_states
    return True

    # for k in range(1, len(word)):
    #     new_state = []
    #     for i in range(len(visited)):
    #         r = visited[i][0]
    #         c = visited[i][1]

    #         neighbor_list = neighbors(r, c, board)
    #         print(f"r, c :", r, c)
    #         print(f"neighbor_list: ", neighbor_list)

    #         for a in neighbor_list:
    #             if a[0] == word[k] and (a[1], a[2]) not in visited:
    #                 visited2 = visited.copy()
    #                 visited2.append((a[1], a[2]))
    #                 # overlap_list.append((a[1], a[2]))
    #                 new_state.append(((a[1], a[2]), visited2))
    #                 print(f"new_state: ", new_state)

    #     if new_state is None:
    #         return False
    #     else:
    #         visited = new_state

    # for a in neighbor_list:
    #     if a[0] == word[1]:
    #         r = a[1]
    #         c = a[2]
    #         overlap_list.append((r, c))
    # if len(overlap_list) == 0:
    #     return False

    # overlap_list = []
    # neighbor_list = neighbors(r, c, board)

    # for a in neighbor_list:
    #     if a[0] == word[2]:
    #         r = a[1]
    #         c = a[2]
    #         overlap_list.append((r, c))
    #     else:
    #         return False

    # for j in range(len(first_word_pos)):
    #     overlap_list = []
    #     for word_index in range(1, len(word)):

    #         r = first_word_pos[j][0]
    #         c = first_word_pos[j][1]

    #         neighbor_list = neighbors(r, c, board)

    #         for k in neighbor_list:
    #             if k[0] == word[word_index]:
    #                 overlap_list.append((k[1], k[2]))

    #         return overlap_list

    # for i in range(len(first_word_pos)):
    #     r = first_word_pos[i][0]
    #     c = first_word_pos[i][1]
    #     visited = [(r, c)]

    #     word_index = 1

    #     print(f"第一個 for 迴圈執行第 {i + 1} 次")

    #     # for word_index in range(1, len(word)):

    #     neighbor_arr = neighbors(r, c, board)

    #     overlap_list = []

    #     for j in neighbor_arr:
    #         # if j[0] == word[word_index] and (j[1], j[2]) not in visited:
    #         r = j[1]
    #         c = j[2]
    #         if board[r][c] == word[word_index]:
    #             overlap_list.append((r, c))

    #         repeat_list = []

    #         repeat_list.append((r, c))

    #     for re in repeat_list:

    #         print(f"第 {j} 次的append {r, c}")
    #         visited.append((r, c))
    #         if len(visited) == len(word):
    #             return True
    #         break

    # print(visited)

    # if len(visited) != len(word):
    #     return False
    # return True


def can_finish(r, c, visited, board, word, k):
    # 要先知道現在是第幾個，是第 k 個
    for i in range(k, len(word)):
        neighbor_arr = neighbors(r, c, board)
        visited.append((r, c))
        return True


def neighbors(r, c, board):
    r_front, r_end = 0, 0
    c_front, c_end = 0, 0

    neighbor_array = []
    board_size = len(board)

    if r == 0:
        r_front = r
        r_end = 1

    else:
        r_front = r - 1
        r_end = r + 1 if r + 1 < board_size else r

    if c == 0:
        c_front = c
        c_end = 1
    else:
        c_front = c - 1
        c_end = c + 1 if c+1 < board_size else c

    for i in range(r_front, r_end + 1):
        for j in range(c_front, c_end + 1):
            if i == r and j == c:
                pass
            else:
                neighbor_array.append((board[i][j], i, j))

    # print(neighbor_array)
    return neighbor_array


testBoard = [
    ["E", "A", "R", "A"],
    ["N", "L", "E", "C"],
    ["I", "A", "I", "S"],
    ["B", "Y", "O", "R"]
]
word1 = "BAILER"

print(find_word(testBoard, word1))
