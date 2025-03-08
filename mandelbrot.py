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


# Part 2 

import numpy as np 
"""Function creates a 2D grid array containing complex numbers evenly spaced between 
    top_left and (not included) bottom_right.  
    """
def get_complex_grid(top_left: complex, bottom_right: complex, step: float) -> np.ndarray:
   
    top_left_real = top_left.real # This line and the next line grabs the real part of the complex number
    bot_right_real = bottom_right.real
    top_left_imag = top_left.imag #This line and the next line grabs the imaginary part of the complex number
    bot_right_imag = bottom_right.imag
    
    """ Imaginary values changing (decreasing) ties to moving down (the y axis)
        Real values changing (increasing) ties to moving to the right (the x axis)"""
    
    our_real_val = np.arange(top_left_real, bot_right_real, step) #Creates  array of real numbers from top_left_real to bot_right_real
    our_imag_val = np.arange(top_left_imag, bot_right_imag, -step) #Creates an array of imaginary numbers from top_left_imag to bot_right_imag

    real_nums = our_real_val.reshape(1,-1) #reshapes into 1 row array
    imag_nums = our_imag_val.reshape(-1,1) #reshapes into 1 column array 

    complex_grid_result = real_nums + 1j*imag_nums #imag_nums multiplied by 1j to make them complex

    return complex_grid_result


#Reference: https://stackoverflow.com/questions/24592803/separate-real-and-imaginary-part-of-a-complex-number-in-python
#Reference: https://saturncloud.io/blog/understanding-the-differences-between-numpy-reshape1-1-and-reshape1-1/#:~:text=When%20you%20use%20reshape(%2D,elements%20in%20your%20original%20array.
    
