def sum_of_intervals(intervals):
    intervals = sorted(intervals)
    interval_length = len(intervals)
    length = 0

    current_start, current_end = intervals[0]

    for i in range(1, interval_length):
        next_start, next_end = intervals[i]

        if next_start < current_end:
            current_end = max(current_end, next_end)
        else:
            length += current_end - current_start
            current_start = next_start
            current_end = next_end

    length += current_end - current_start
    return length


print(sum_of_intervals([(1, 5), (7, 10)]))
