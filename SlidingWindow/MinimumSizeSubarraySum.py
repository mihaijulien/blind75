"""
Given an array of positive integers a and a positive number K, find the length of the smallest contiguous subarray whose
sum is greater than or equal to K. Return 0 if no such subarray exists.

eq.

Input: a = [2, 1, 4, 3, 2, 5], K = 7
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to '7' is [4, 3]
"""
from typing import List
import sys


def minimum_size_subarray_sum(a: List[int], k: int) -> int:
    window_start, window_end = 0, 0
    min_subarray_length = sys.maxsize
    window_sum = 0

    for window_end in range(0, len(a)):
        window_sum += a[window_end]

        while window_sum >= k:
            min_subarray_length = min(min_subarray_length, window_end - window_start + 1)
            window_sum -= a[window_start]
            window_start += 1

    return min_subarray_length


if __name__ == '__main__':
    a = [2, 1, 4, 3, 2, 5]
    k = 7
    print(minimum_size_subarray_sum(a, k))  # 2 [4,3] or [2,5]

    a2 = [3, 4, 1, 1, 6]
    k2 = 8

    print(minimum_size_subarray_sum(a2, k2))  # 3 [3, 4, 1] or [1, 1, 6]

