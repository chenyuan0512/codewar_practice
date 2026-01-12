def dbl_linear(n):
    ans_list = [1]

    y_index, z_index = 0, 0
    

    while len(ans_list) <= n:
        y = 2 * ans_list[y_index] + 1
        z = 3 * ans_list[z_index] + 1

        if y < z:
            ans_list.append(y)
            y_index += 1
        elif z < y:
            ans_list.append(z)
            z_index += 1
        else:
            ans_list.append(y)
            y_index += 1
            z_index += 1

    return ans_list[-1]


n = 50
print(dbl_linear(n))
