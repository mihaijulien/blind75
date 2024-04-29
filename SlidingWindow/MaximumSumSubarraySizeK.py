'''
Given an array of positive integers, and a positive number k, find the maximum sum of any contiguous subarray of size k.
Input: [3, 5, 2, 1, 7], k=2
Output: 8
Explanation: Subarray with maximum sum is [1, 7].
'''
from typing import List


def findMaximumSubarrayOfSizeK(array: List[int], k: int) -> int:
    if k == 0 or len(array) == 0:
        return 0

    max_sum = -1
    window_start = 0
    window_sum = 0

    for window_end in range(0, len(array) - 1):
        window_sum += array[window_end]

        if window_end - window_start + 1 == k:  # when we hit the window size, update maximum sum, and slide the window
            max_sum = max(window_sum, max_sum)
            window_sum -= array[window_start]
            window_start += 1

    return max_sum


if __name__ == '__main__':
    print(findMaximumSubarrayOfSizeK([3, 5, 2, 1, 7], 2))  # 8
    print(findMaximumSubarrayOfSizeK([4, 2, 3, 5, 1, 2], 3))  # 10

