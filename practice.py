def snail(snail_map):

    # n = len(snail_map) # 因為 snail map 是 n * n 的，所以直接這樣寫

    ans_list = []

    n, top, bottom, left, right = len(
        snail_map), 0, len(snail_map)-1, 0, len(snail_map)-1

    # print(snail_map[0][0:2])  # [1, 2]

    while top <= bottom and left <= right:
        # print(top, bottom)

        for i in range(left, right+1, 1):
            element = snail_map[top][i]
            ans_list.append(element)
        top += 1

        for i in range(top, bottom+1, 1):
            element = snail_map[i][right]
            # print(element)
            ans_list.append(element)
        right -= 1

        for i in range(right, left-1, -1):
            element = snail_map[bottom][i]
            ans_list.append(element)
        bottom -= 1

        for i in range(bottom, top-1, -1):
            element = snail_map[i][left]
            ans_list.append(element)
        left += 1
        # print(top, bottom, left, right)
        # print(ans_list)

    return ans_list


array = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]
print(snail(array))
