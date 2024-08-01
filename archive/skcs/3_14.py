def sum_arr(arr):
    max_sum = -100000

    for i in range(4):
        for j in range(4):
            temp = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + \
                   arr[i + 2][j + 2]

            if temp > max_sum:
                max_sum = temp
    return max_sum

print(sum_arr([[-9, -9, -9, 1, 1, 1], [0, -9, 0, 4, 3, 2], [-9, -9, -9, 1, 2, 3], [0, 0, 8, 6, 6, 0], [0, 0, 0, -2, 0, 0],
         [0, 0, 1, 2, 4, 0]]))
