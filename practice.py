def sum_for_list(lst):
    initial_list = lst
    ans_list = []

    # 1. 先做質因數分解
    final_ans_dict = dict()

    for n in initial_list:
        i = abs(n)
        factor = 2

        while factor * factor <= i:  # 代表還有質數可以檢查

            if i % factor == 0:
                if factor not in final_ans_dict:
                    final_ans_dict[factor] = 0
                final_ans_dict[factor] += n
            while i % factor == 0:
                i //= factor
            factor += 1

        if i > 1:
            if i not in final_ans_dict:
                final_ans_dict[i] = 0
            final_ans_dict[i] += n

    ans_list = sorted([[key, value] for key, value in final_ans_dict.items()])

    return ans_list


print(sum_for_list([15, 21, 24, 30, 45]))
