def product(a, b):
    """
    return the product of a and b using only + and - operators
    """
    if type(b) is not int:
        raise TypeError('second argument must be an integer')

    if b == 1:
        return a
    else:
        return a + product(a, b-1)
