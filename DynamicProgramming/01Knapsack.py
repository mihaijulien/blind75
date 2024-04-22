'''
You are given nn items whose weights and values are known, as well as a knapsack to carry these items. The knapsack cannot carry more than a certain maximum weight, known as its capacity.

You need to maximize the total value of the items in your knapsack, while ensuring that the sum of the weights of the selected items does not exceed the capacity of the knapsack.

If there is no combination of weights whose sum is within the capacity constraint, return 0.

eg.

capacity: 30
weights: [10, 20, 30]
values:  [22, 33, 44]

Output: 55 (22 + 33)

'''

class Solution:
    def find_max_knapsack_profit(capacity: int, weights: List[int], values: List[int]) -> int:
        n = len(values)

        if capacity < 0:
            return 0

        knapsack = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

        for i in range(0, n + 1):
            for j in range(0, capacity + 1):
                if i == 0 or j == 0:
                    knapsack[i][j] = 0
                elif weights[i - 1] <= j:
                    knapsack[i][j] = max(values[i - 1] + knapsack[i - 1][j - weights[i - 1]],
                                         knapsack[i - 1][j])
                else:
                    knapsack[i][j] = knapsack[i - 1][j]

        return knapsack[n][capacity]

