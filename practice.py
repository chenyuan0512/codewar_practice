def hamming(n):
    ans_list = [1]
    power_2, power_3, power_5 = 0, 0, 0

    for i in range(n-1):

        next_r2 = ans_list[power_2] * 2
        next_r3 = ans_list[power_3] * 3
        next_r5 = ans_list[power_5] * 5
        next_row_list = [next_r2, next_r3, next_r5]

        smallest = min(next_row_list)

        ans_list.append(smallest)

        if next_r2 == smallest:
            power_2 += 1
        if next_r3 == smallest:
            power_3 += 1
        if next_r5 == smallest:
            power_5 += 1

    return ans_list[-1]


print(hamming(5000))
