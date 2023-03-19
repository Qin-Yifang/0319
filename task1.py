# Define all functions for Task 1 here.
# Any necessary import statements should go at the top of each module.
# For example, if you need Numpy in your Task 1 functions:
import numpy as np
import random
from typing import List
from collections import Counter

# 将算法推广为找到 𝑝 次方的向下取整根
def floor_root(number: int, power: int = 2) -> int:
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
    111
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
    return int((x + 0.5)**(1/2))

def check_floor_root(number: int, root: int, power: int = 2) -> bool:
    if power == 1:
        return number == root
    elif power == 2:
        return root**2 <= number < (root+1)**2
    else:
        lower_bound = root**power
        upper_bound = (root+1)**power
        return lower_bound <= number < upper_bound

def random_number(digits: int) -> int:
    if digits <= 0:
        return 0
    else:
        lower_bound = 10**(digits-1)
        upper_bound = 10**digits - 1
        return random.randint(lower_bound, upper_bound)

def unsafe_failure_rate(number_sizes: List[int], samples: int = 500) -> List[float]:
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
