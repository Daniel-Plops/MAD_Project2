def get_escape_time(c: complex, max_iterations: int) -> int | None:
    """
    :param c: c is the complex number from which we will be finding the iterations (if it all) until we determine
    whether c is guaranteed to tend toward infinity.
    :param max_iterations: max_iterations is the maximum number of iterations we will test to see if c is
    guaranteed to tend toward infinity.
    :return: An int indicating the number of iterations it took to determine whether c is guaranteed to tend toward
    infinity (i.e. its escape time) or None if it was never guaranteed within max_iterations.
    """
    # This helper function checks if a complex number is guaranteed to tend toward infinity within the mandelbrot set.
    def tends_toward_infinity(comp: complex) -> bool:
        """
        :param comp: The complex number we are checking to see if its magnitude is above 2, which means it is
        guaranteed to tend toward infinity under the mandelbrot set.
        :return: A boolean indicating whether comp is guaranteed to tend toward infinity under the mandelbrot set.
        """
        return (comp.real**2 + comp.imag**2)**0.5 > 2

    # We used 'current_z' to track the current complex number being calculated in the mandelbrot set.
    current_z = c

    # If the magnitude of current_z (c in this case) is already greater than 2, it took 0 iterations for c to be
    # guaranteed to tend toward infinity.
    if tends_toward_infinity(current_z):
        return 0

    # This is a for loop that tracks the number of iterations within the mandelbrot set c goes through before being
    # guaranteed to reach infinity. The for loop iterates through [1:max_iterations] calculating a new current_z every
    # iteration and then checking if its magnitude guarantees it will tend toward infinity and returns the iteration
    # if so.
    for iteration in range(1, max_iterations+1, 1):
        current_z = current_z**2 + c
        if tends_toward_infinity(current_z):
            return iteration

    # If the code reaches this point it is because current_z's magnitude was never above 2, which means it was never
    # guaranteed to tend toward infinity, thus we return None.
    return None