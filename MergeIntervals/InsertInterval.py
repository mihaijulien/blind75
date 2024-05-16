"""
Given a sorted list of nonoverlapping intervals and a new interval, your task is to insert the new interval into the
correct position while ensuring that the resulting list of intervals remains sorted and nonoverlapping. Each interval
is a pair of nonnegative numbers, the first being the start time and the second being the end time of the interval.
"""
from typing import List


def insert_interval(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    before = []
    after = []

    for interval in intervals:

        if interval[1] < new_interval[0]:
            before.append(interval)

        elif interval[0] > new_interval[1]:
            after.append(interval)

        else:
            new_interval[0] = min(new_interval[0], interval[0])
            new_interval[1] = max(new_interval[1], interval[1])

    res = before + [new_interval] + after
    return res


if __name__ == '__main__':
    print(insert_interval([[1,3],[6,9]],  [2,5]))  # output: [[1,5][6,9]]
    print(insert_interval([[1, 3], [6, 9]], [2, 11]))
