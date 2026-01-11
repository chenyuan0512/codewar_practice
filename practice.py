def format_duration(seconds):

    ans_str = ""

    if seconds == 0:
        return "now"

    minute = 60
    hour = minute * 60
    day = hour * 24
    year = day * 365

    unit_dict = [("year", year), ("day", day),
                 ("hour", hour), ("minute", minute), ("second", 1)]
    ans_list = []

    for i in range(len(unit_dict)):
        element = seconds // unit_dict[i][1]
        seconds %= unit_dict[i][1]

        if element == 1:
            ans_list.append(str(element) + " " + unit_dict[i][0])
        elif element > 1:
            ans_list.append(str(element) + " " + unit_dict[i][0] + "s")

    if len(ans_list) == 1:
        ans_str += ans_list[0]
    elif len(ans_list) == 2:
        ans_str += (ans_list[0] + " and " + ans_list[1])
    else:
        ans_str += (", ".join(i for i in ans_list[:-1]
                              ) + " and " + ans_list[-1])

    return ans_str


total_time = 15729880
print(format_duration(total_time))
