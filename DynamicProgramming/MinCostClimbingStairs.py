'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        optimal = [0] * (len(cost) + 1)
        
        if len(cost) >= 0:
            optimal[0] = cost[0]
        if len(cost) >= 1:
            optimal[1] = cost[1]
            
        for i in range(2, len(cost)+1):
            if i == len(cost):
                c = 0
            else:
                c = cost[i]
            
            optimal[i] = min(optimal[i-1] , optimal[i-2]) + c
            
        return optimal[len(cost)]
