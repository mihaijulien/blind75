'''
Given a bitonic array of numbers and a target value, find the index of the target value in the bitonic array in O(log n) time.

A bitonic array is an array that is first increasing and then decreasing.
'''
from typing import List


def search_bitonic_array(arr: List[int], target: int) -> int:

    def find_max_element(array: List[int]) -> int:
        start = 0
        end = len(arr) - 1

        while start <= end:
            mid = (start + end) // 2

            # no increasing -> mid == 0 && no decreasing mid == len(arr) - 1
            if (mid == 0 or arr[mid] > arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] > arr[mid + 1]):
                return mid
            elif arr[mid] < arr[mid - 1]:
                end = mid - 1
            else:
                start = mid + 1

        return -1

    def binary_search(arr: List[int], start: int, end: int, key: int) -> int:

        while start <= end:
            mid = (start + end) // 2

            if key == arr[mid]:
                return mid
            elif key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

        return -1

    max_index = find_max_element(arr)

    # binary search in both sorted arrays
    target_index = binary_search(arr, 0, max_index, target)
    if target_index != -1:
        return target_index
    return binary_search(arr, max_index + 1, len(arr) - 1, target)


if __name__ == '__main__':

    print(search_bitonic_array([2, 4, 8, 10, 7, 6, 1], 6)) # 5
    print(search_bitonic_array([2, 4, 6, 8, 10, 5, 3, 1], 30)) # -1

