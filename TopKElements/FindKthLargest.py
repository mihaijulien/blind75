'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        
        for n in nums:
            heapq.heappush(pq, n)
			
            if len(pq) > k:
                heapq.heappop(pq)
        
        return pq[0]
