# Define all functions for Task 3 here.
import numpy as np

def define_Ka(a):
    """
    Returns a function that evaluates the expression 1 / sqrt(a - cos(x)) for a given value of a.
    
    Args:
        a (float): Value of a in the expression 1 / sqrt(a - cos(x)).
    
    Returns:
        Ka (function): A function that takes a numerical value x and evaluates the expression 1 / sqrt(a - cos(x)).
    """
    @counter
    def Ka(x):
        return 1 / np.sqrt(a - np.cos(x))
    return Ka

def Kintegral(Ka, n):
    """
    Computes the integral of the function Ka(x) using the composite trapezoidal rule.
    
    Args:
        Ka (function): A function that takes a numerical value x and evaluates an expression.
        n (int): The number of nodes to use in the composite trapezoidal rule.
        
    Returns:
        I (float): The computed integral of Ka(x).
    """
    # Calculate the nodes and step size of the composite trapezoidal rule
    x, h = np.linspace(-np.pi, np.pi, n, retstep=True)
    
    # Evaluate Ka at the nodes and sum the terms
    y = Ka(x)
    I = h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])
    
    return I


def counter(original_f):
    """
    A decorator function that counts the number of times a function is called.
    
    Args:
        original_f (function): The original function to be counted.
        
    Returns:
        decorated_f (function): A decorated function that has an additional attribute .evals which stores the number of times the original function is evaluated.
    """
    # Define our new, decorated function, with added features
    def decorated_f(x):
        # Increment the number of .evals (depending on whether x is a number or an array)
        try:
            l = len(x)
        except:
            l = 1
        decorated_f.evals += l
        
        # Still return the result of the original function
        return original_f(x)
    
    # Initialise the number of evaluations, store it in a new .evals attribute
    decorated_f.evals = 0
    
    # Return the new, decorated function, which now has a .evals value
    return decorated_f

