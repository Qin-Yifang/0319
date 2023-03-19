# Define all functions for Task 1 here.
# Any necessary import statements should go at the top of each module.
# For example, if you need Numpy in your Task 1 functions:
import numpy as np
import random
from typing import List
from collections import Counter

# 将算法推广为找到 𝑝 次方的向下取整根
def floor_root(number: int, power: int = 2) -> int:
    """
    Compute the floor of the p-th root of a non-negative integer.

    Args:
    - number: non-negative integer whose p-th root to be computed
    - power: positive integer indicating the root (default: 2)

    Returns:
    - the largest integer r such that r^p <= number.

    Example:
    >>> floor_root(10, 3)
    2
    >>> floor_root(100, 2)
    10
    """
    if number == 0 or number == 1:
        return number

    left, right = 1, number
    result = None

    while left <= right:
        mid = (left + right) // 2

        if mid ** power == number:
            return mid

        if mid ** power < number:
            left = mid + 1
            result = mid
        else:
            right = mid - 1

    return result


# 使用二分查找算法来计算一个正整数的向下取整平方根
def floor_square_root(number: int) -> int:
    """
    Compute the floor of the square root of a non-negative integer.

    Args:
    - number: non-negative integer whose square root to be computed

    Returns:
    - the largest integer r such that r^2 <= number.

    Example:
    >>> floor_square_root(10)
    3
    >>> floor_square_root(100)
    10
    """
    if number == 0 or number == 1:
        return number

    left, right = 1, number
    result = None

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == number:
            return mid

        if mid * mid < number:
            left = mid + 1
            result = mid
        else:
            right = mid - 1

    return result

def unsafe_floor_sqrt(x):
    """
    A simple implementation of square root that uses an approximate formula.
    The implementation is not robust and may fail for certain inputs.

    Args:
    - x: a non-negative number whose square root to be computed

    Returns:
    - the approximate square root of x

    Example:
    >>> unsafe_floor_sqrt(10)
    3
    >>> unsafe_floor_sqrt(100)
    10
    """
    return int((x + 0.5)**(1/2))

def check_floor_root(number: int, root: int, power: int = 2) -> bool:
    """
    Check whether r is the pth floor root of n, i.e., r^p <= n < (r+1)^p.

    Args:
    - number: non-negative integer whose pth floor root is to be checked
    - root: integer that may be the pth floor root of number
    - power: positive integer indicating the root (default: 2)

    Returns:
    - True if root is the pth floor root of number, False otherwise.

    Example:
    >>> check_floor_root(10, 3)
    True
    >>> check_floor_root(100, 10)
    True
    """
    if power == 1:
        return number == root
    elif power == 2:
        return root**2 <= number < (root+1)**2
    else:
        lower_bound = root**power
        upper_bound = (root+1)**power
        return lower_bound <= number < upper_bound

def random_number(digits: int) -> int:
    """
    Generate a random non-negative integer with exactly digits decimal digits.

    Args:
    - digits: positive integer indicating the number of decimal digits

    Returns:
    - a random non-negative integer with exactly digits decimal digits.

    Example:
    >>> random_number(3)
    746
    >>> random_number(5)
    43568
    """
    if digits <= 0:
        return 0
    else:
        lower_bound = 10**(digits-1)
        upper_bound = 10**digits - 1
        return random.randint(lower_bound, upper_bound)

def unsafe_failure_rate(number_sizes: List[int], samples: int = 500) -> List[float]:
    """
    Determine an approximate failure rate for the unsafe_floor_sqrt() function
    by generating random numbers with different numbers of digits and checking
    whether the function produces correct results. The function returns a list
    of failure rates for each tested number size.

    Args:
    - number_sizes: a list of positive integers indicating the number of digits of random numbers to be tested
    - samples: the number of random numbers to be tested for each number size (default: 500)

    Returns:
    - a list of floating-point numbers between 0 and 1 representing the failure rates of unsafe_floor_sqrt() for
      each number size.
    """
    failure_rates = []
    for digits in number_sizes:
        failures = 0
        for _ in range(samples):
            n = random_number(digits)
            r = unsafe_floor_sqrt(n)
            if not check_floor_root(n, r):
                failures += 1
        failure_rate = failures / samples
        failure_rates.append(failure_rate)
    return failure_rates