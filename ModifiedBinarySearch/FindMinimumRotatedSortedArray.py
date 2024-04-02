'''
You’re given a rotated sorted array, arr, of length n, that is rotated clockwise between 1 and n times.

For example,

    Before rotation, arr = [1,2,3,4,5,6,7,8]

    After 33 rotations, the array becomes [6,7,8,1,2,3,4,5].

For the given array, your task is to find the minimum element of this array.

 '''

class Solution:
    def find_min_in_rotated_array(self, arr: List[int])-> int:
        low = 0
        high = len(arr)

        min = arr[0]

        while high >= low:
            mid = low + (high - low) // 2
            if arr[mid] > arr[mid + 1]:
                return arr[mid + 1]

            if arr[mid] < arr[mid - 1]:
                return arr[mid]

            if arr[mid] > arr[low]:
                low = mid + 1
            else:
                high = mid - 1
        return 0