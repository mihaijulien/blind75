"""
Given an array of integers a, and a positive integer k, find the first negative integer for each and
every window (contiguous subarray) of size k. If a window does not contain a negative integer, then print 0 for that window.

Input: a[] = {-5, 1, 2, -6, 9}, k = 2
Output : -5 0 -6 -6

Explanation: First negative integer in every window of size 2
{-5, 1} = -5
{1, 2} = 0 (does not contain a negative integer)
{2, -6} = -6
{-6, 9} = -6
"""
from typing import List
import queue


def first_negative_every_window(a: List[int], k: int) -> List[int]:
    window_start, window_end = 0, 0
    q = queue.Queue()
    first_negative = []
    idx = 0
    for window_end in range(0, len(a)):
        if a[window_end] < 0:
            q.put(a[window_end])
        if window_end - window_start + 1 == k:
            window_start += 1
            if q.empty():
                first_negative.append(0)
            else:
                first_negative.append(q.get())

    return first_negative


if __name__ == '__main__':
    a = [-5, 1, 2, -6, 9]
    k = 2

    print(first_negative_every_window(a, k))
