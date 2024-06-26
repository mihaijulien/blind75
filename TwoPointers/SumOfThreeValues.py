'''
Given an array of integers, nums, and an integer value, target, determine if there are any three integers in nums whose sum is equal to the target, 
that is, nums[i] + nums[j] + nums[k] == target. Return TRUE if three such integers exist in the array. Otherwise, return FALSE.

Constraints:

    3 ≤ nums.length ≤ 500
    −10^3 ≤ nums[i] ≤ 10^3
    −10^3 ≤ target ≤ 10^3
'''

class Solution:
    def find_sum_of_three(self, nums: List[int], target: int) -> bool:
        nums.sort()

        for i in range(0, len(nums) - 2):
            low = i + 1
            high = len(nums) - 1

            while low < high:
                triplet = nums[i] + nums[low] + nums[high]

                if triplet == target:
                    return True

                elif triplet < target:
                    low += 1

                else:
                    high -= 1

        return False