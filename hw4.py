# factorial
""" Compute factorial of n

    Args:
        n (int)

    Returns:
        int: factorial of n
    """


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Wallis function
def wallisPi(n):
    """ Compute the approximation of pi/2 with n iterations
        using the Wallis's formula

    Args:
        n (int)

    Returns:
        float: approximation of pi/2
    """
    if n == 0:
        return 0
    elif n == 1:
        return 4 / 3
    else:
        return 4 * (n ** 2) / (2 * n - 1) / (2 * n + 1) * wallisPi(n - 1)


#  Gregory function
def gregoryPi(n):
    """ Compute the approximation of pi/4 with n iterations
        using the Gregory's formula

    Args:
        n (int)

    Returns:
        float: approximation of pi/4
    """
    if n == 0:
        return 1
    else:
        return (-1 ** 2) * 1 / (2 * n - 1) + gregoryPi(n - 1)


# Ramanujan function
def ramanujanPi(n):
    """ Compute the recursive part of the pi approximation
    defined by Ramanujan

    Args:
        n (int)

    Returns:
        float: part of the denominator of Ramanujan's approximation
    """
    if n == 0:
        return 1103
    else:
        return (((factorial(4 * n)) / (factorial(n) ** 4)) * ((1103 + 26390 * n) / ((4 * 99) ** (4 * n)))) + ramanujanPi(n - 1)


# compute distance
def distComputRec(lst, q, lst_dist):
    """ Compute all the distances between a query value
    and all the elements in a list.
    And return the distances in a list of distance

    Args:
        lst (list): input list of element
        q (int/float): query value
        lst_dist (list): list containing the resulting distances
        This last argument should be initialized with an empty list []

    Returns:
        void function
    """
    if len(lst) < 1:
        print(lst_dist)
    else:
        lst_dist.append(abs(lst[0] - q))
        distComputRec(lst[1:], q, lst_dist)


# compute min
def findMinRec(lst, min=None):
    """ Find minimum element in a list

    Args:
        lst (list): input list containing numerical values
        min (int/float): keeping track of the minimum value (initialized to None)

    Returns:
        int/float: returns minimum value in the list
    """
    if len(lst) == 1 and min is not None:
        return min
    elif len(lst) == 1 and min is None:
        return findMinRec(lst, lst[0])
    elif len(lst) > 1 and min is None:
        return findMinRec(lst[1:], lst[0])
    else:
        if lst[0] < min:
            return findMinRec(lst[1:], lst[0])
        else:
            return findMinRec(lst[1:], min)


# compute occurences
def countOccurenceRec(lst, query, count=0):
    """ Count the number of occurence of a query in a list

    Args:
        lst (list): input list containing numerical values
        query (int/float): query value for which we count the number of occurences
        count (int): a counter we increment when we meet an element == query
        The latest argument is initialized to zero

    Returns:
        int: number of occurences of the query in the list
    """
    if len(lst) < 1:
        return count
    else:
        if lst[0] == query:
            return countOccurenceRec(lst[1:], query, count + 1)
        else:
            return countOccurenceRec(lst[1:], query, count)


# check sort
def checkSortRec(lst):
    """ Check is the list is properly sorted

    Args:
        lst (list): input list containing numerical values

    Returns:
        bool: True if the list is sorted, otherwise False
    """
    if len(lst) < 2:
        return True
    else:
        if lst[0] > lst[1]:
            return False
        else:
            return checkSortRec(lst[1:])


# MAIN
def main():
    # compute pi
    import math
    print(math.pi)
    print(wallisPi(900) * 2)
    print(gregoryPi(900) * 4)

    print(9801 / (2 * (2 ** 0.5) * ramanujanPi(100)))

    # compute distance
    lst = [45, 10, 97, 103, 1, 52, 100]
    query = 1
    lst_dist = []
    distComputRec(lst, query, lst_dist)
    print(lst_dist)

    # find min
    min_val = findMinRec(lst)
    print(min_val)

    # count occurence
    lst = [45, 10, 97, 10, 1, 10, 100]
    print(countOccurenceRec(lst, 10))

    # check sorted list
    lst1 = [45, 10, 97, 10, 1, 10, 100]
    lst2 = [1, 2, 3, 4, 5, 6, 7]
    print(checkSortRec(lst1))
    print(checkSortRec(lst2))



main()  # Run the main code
