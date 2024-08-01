# Name:Yohan Lim
# SBUID:114741891

# TODO: Print the following information
# Max element, Min element, Trace (only if 'm' is a square matrix)
# Do not modify the following nested for-loop
# Do not add other functions or loops
def print_matrix_info(m):
    max_element = m[0][0]
    min_element = m[0][0]
    trace_sum = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] > max_element:
                max_element = m[i][j]
            elif m[i][j] < min_element:
                min_element = m[i][j]

            if j == i:
                trace_sum += m[i][j]

    if len(m) != len(m[0]):
        trace_sum = None

    print(max_element, min_element, trace_sum)

# TODO: Return the transposed matrix
def transpose(m):
    final = []
    for i in range(len(m[0])):
        temp = []
        for j in range(len(m)):
            temp.append(m[j][i])
        final.append(temp)
    return final


mtx = [[2, 3, 4], [0, 0, 0], [1, 2, 3], [5, 7, -1]]

print_matrix_info(mtx) # Trace should be None, Max is 7, Min is -1

print(transpose(mtx)) # [[2, 0, 1, 5], [3, 0, 2, 7], [4, 0, 3, -1]]
