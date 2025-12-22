def longest_slide_down(pyramid):

    for i in range(len(pyramid) - 2, -1, -1):
        for j in range(i+1):
            print(i, j)
            left = pyramid[i][j] + pyramid[i+1][j]
            right = pyramid[i][j] + pyramid[i+1][j+1]
            pyramid[i][j] = max(left, right)

    return pyramid[0][0]


print(longest_slide_down([[10], [10, 20], [10, 10, 20], [10, 90, 10, 20]]))
