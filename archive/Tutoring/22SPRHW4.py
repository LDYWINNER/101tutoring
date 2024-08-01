# Name:
# SBUID:
# Remove the ellipses (...) when writing your solutions.
# ---------------------------- Q1 ---------------------------------------
# TODO: Return the Euclidean distance between two points x and y using a 'while' loop.
# Do not assume that x and y are 2-dimensional.
def dist(x, y):
    res = []
    i = 0
    while i < len(x):
        temp = x[i] - y[i]
        res.append(temp)
        i += 1

    final = 0
    j = 0
    while j < len(res):
        final += (res[j] ** 2)
        j += 1
    return final ** (1/2)


# ---------------------------- Q2 ---------------------------------------
# TODO: Implement the nearest neighbor search algorithm using dist() above.
# i.e., find and return the closest point in 'lst' to 'q'.
def nearest_neighbor(lst, q):
    min = 1000000000
    min_index = -1
    k = 0
    while k < len(lst):
        temp = dist(q, lst[k])
        if temp < min:
            min = temp
            min_index = k
        k += 1
    return lst[min_index]



# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.
db = [[2, 3], [0, 0], [1, 6], [5, 2], [9, 10]]
q = [0.5, 0.1]
print(dist(db[0], db[1])) # Should print out the square root of 13

print(nearest_neighbor(db, q)) # Should print out [0, 0]
