import math

def elevation(x):
    """
    This function computes the elevation of a given position in the landscape.
    Args:
        x (float): The position for which to compute the elevation.
    Returns:
        float: The elevation at the given position.
    """
    return float((x ** 2) + 10 * math.sin(x))

def slope(x):
    """
    This function computes the slope at a given position.
    Args:
        x (float): The position for which to compute the derivative.
    Returns:
        float: The derivative of the elevation at the given position.
    """
    return float((2 * x) + 10 * math.cos(x))

