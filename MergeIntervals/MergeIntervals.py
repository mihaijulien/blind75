"""
Given a collection of intervals, merge all overlapping intervals.

intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
"""

from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()

    merged_intervals = [intervals[0]]  # add the first interval as starting interval for merging

    for interval in intervals[1:]:  # start from second element
        start = interval[0]
        end = interval[1]
        last_merged_interval = merged_intervals[-1]
        if last_merged_interval[1] < start:  # no overlap, add current interval as it is
            merged_intervals.append(interval)
        else:
            last_merged_interval[1] = max(last_merged_interval[1], end)  # extend last merged interval's end time

    return merged_intervals


if __name__ == '__main__':
    print(str(merge_intervals([[1, 3], [8, 10], [15, 18], [2, 6]])))  # output: [[1, 6], [8, 10], [15, 18]]
    print(str(merge_intervals([[1, 6], [8, 10]])))  # [[1, 6], [8, 10]]
    print(str(merge_intervals([[1, 4], [0, 4]]))) # [0,4]

