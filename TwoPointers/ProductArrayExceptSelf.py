'''
You’re given an integer array, arr. Return a resultant array so that res[i] is equal to the product of all the elements of arr except arr[i].

Write an algorithm that runs in O(n) time without using the division operation.
'''

class Solution:
    def product_except_self(self, nums: List[int]) -> int:
    
    # the product of elements to the left of each index and the product of elements to the right of each index
    res = [1] * len(nums)
    left = 0
    right = len(nums) - 1
    left_product, right_product= 1, 1

    while right >= 0 and left < len(nums):
        res[left] *= left_product
        res[right] *= right_product

        left_product *= nums[left]
        right_product *= nums[rright]

        left += 1
        right -= 1