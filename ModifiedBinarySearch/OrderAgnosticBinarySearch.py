from typing import List


def agnostic_binary_search(arr: List[int], key: int) -> int:
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if key == arr[mid]:
            return mid
        elif (arr[start] < arr[end] and key < arr[mid]) or (arr[start] > arr[end] and key > arr[mid]):
            end = mid - 1
        else:
            start = mid + 1

    return -1


if __name__ == '__main__':
    input_asc = [2, 8, 11, 19]
    key1 = 11
    print(agnostic_binary_search(input_asc, key1))  # 2

    input_desc = [32, 28, 17, 9, 3]
    key2 = 9
    print(agnostic_binary_search(input_desc, key2))  # 3

