'''
A bitonic array is an array that is first increasing and then decreasing. Given an array of numbers which is
first increasing and then decreasing, find the maximum value in the array.
'''
from typing import List


def find_maximum_bitonic(arr: List[int]) -> int:
    # the maximum element is the only element greater than both of its adjacent elements
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        # no increasing -> mid == 0 && no decreasing mid == len(arr) - 1
        if (mid == 0 or arr[mid] > arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] > arr[mid + 1]):
            return arr[mid]
        elif arr[mid] < arr[mid - 1]:
            end = mid - 1
        else:
            start = mid + 1

    return -1


if __name__ == "__main__":
    input = [2, 4, 6, 8, 10, 3, 1]
    print(find_maximum_bitonic(input))  # 10

    # no decreasing
    input2 = [10, 20, 30, 40, 50]
    print(find_maximum_bitonic(input2))

    # no increasing
    input3 = [100, 80, 60, 40, 20, 0]
    print(find_maximum_bitonic(input3))

