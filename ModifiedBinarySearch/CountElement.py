'''
Given a sorted array of integers and a target element.
Find the number of occurrences of the target in the array. You must write an algorithm with O(log n) runtime complexity.
'''
from typing import List


# variation of first and last position of an element in a sorted array
def element_frequency(arr: List[int], key: int) -> int:
    def binary_search_first_pos(arr: List[int], key: int) -> int:
        start = 0
        end = len(arr) - 1
        first_position = -1

        while start <= end:
            mid = (start + end) // 2

            if mid == arr[mid]:
                first_position = mid
                end = mid - 1  # look further to find even smaller positions
            elif key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

        return first_position

    def binary_search_last_pos(arr: List[int], key: int) -> int:
        start = 0
        end = len(arr) - 1
        last_position = -1

        while start <= end:
            mid = (start + end) // 2

            if mid == arr[mid]:
                last_position = mid
                start = mid + 1
            elif key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

        return last_position

    first_position = binary_search_first_pos(arr, key)
    last_position = binary_search_last_pos(arr, key)

    if last_position != -1 and first_position != -1:
        return last_position - first_position + 1
    else:
        return 0


if __name__ == '__main__':
    input_twice = [1, 1, 2, 2, 2, 2, 3]
    key = 1
    print(element_frequency(input_twice, key))  # 2

    not_found = [1, 1, 2, 2, 2, 2, 3]
    key2 = 4
    print(element_frequency(not_found, key2))  # 0

