def next_bigger(n):
    n = [i for i in str(n)]

    index = len(n) - 1

    # 從個位和十位開始比
    # 如果個位比十位大
    #     就交換位置
    # 沒有比較大(一樣或小)
    #     維持原樣
    # 回到十位和百位比，重複下去直到最高位

    while index > 0:
        if n[index-1] < n[index]:  # 從後面看回來，右邊比較大
            turning_points = n[index-1]

            min_point = max(n[index:])

            for i in n[index:]:
                if i > turning_points and i < min_point:
                    print(i, min_point)
                    min_point = i

            min_point_index = n[index:].index(min_point) + index

            n[index-1] = min_point
            n[min_point_index] = turning_points

            n[index:] = sorted(n[index:])
            return int("".join(n))
        index -= 1
    return -1


print(next_bigger(414))
