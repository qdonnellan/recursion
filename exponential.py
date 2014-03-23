def exponential(x, n):
    """
    return the result of x**n

    if n was a negative number, then this would loop (recursively) for ever
    thus, I have added an exception handler for negative values of n
    """
    if n < 0:
        raise ValueError("n must not be negative")

    if n == 0:
        # this is the base case, if n==0 return 1
        return 1
    else:
        # if n != 0, return the result of x times the subsequent recursions
        # For example: 3^7 = 3*(3^6) and so forth
        return x * exponential(x, n-1)
