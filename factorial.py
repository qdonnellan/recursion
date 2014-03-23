def factorial(n):
    """
    return the factorial of an integer n
    """

    # here we handle potential problems
    if type(n) is not int:
        raise TypeError ("n must be an integer")

    if n < 0:
        raise ValueError("n must be positive")


    # and here is the math
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
