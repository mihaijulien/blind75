'''
Given a sorted integer array, nums, and an integer value, target, the array is rotated by some arbitrary number. Search and return the index of target in this array. If the target does not exist, return -11.

An original sorted array before rotation is given below:
[1 10 20 47 59 63 75 88 99 107 120 133 155 162 176 188 199 200 210 222]

After rotating this array 6 times, it changes to:
[176 188 199 200 210 222 1 10 20 47 59 63 75 88 99 107 120 133 155 162]

Constraints:

    All values in nums are unique.
    The values in nums are sorted in ascending order.
    The array may have been rotated by some arbitrary number.
'''

class Solution:
    def binary_search_rotated(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid

            # low to mid is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target and target < nums[mid]:
                    high = mid - 1 # target is within the sorted first half of the array
                else:
                    low = mid - 1
            # mid to high is sorted
            else:
                if nums[mid] < target and target <= nums[high]:
                    low = mid + 1 # target is within the sorted second half of the array
                else:
                    high = mid - 1

        return -1