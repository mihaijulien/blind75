'''
You’re given an integer array height of length n, and there are n vertical lines drawn such that the two endpoints of the ith line are (i,0) and (i, height[i]).

Find two lines from the input array that, together with the x-axis, form a container that holds as much water as possible. Return the maximum amount of water a container can store.

Constraints:

    n = height.length

    2 ≤ n ≤ 10^3

    0 ≤ height[i] ≤10^3

    eg.

    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        start = 0
        end = len(height) - 1

        for i in range(0, len(height)):
            width = end - start
            max_area = max(max_area, min(heigh[start], height[end]) * width)

            if height[start] <= height[end]:  #move the shorter vertical line inward by one step
                start+=1
            else:
                end-=1

        return max_area