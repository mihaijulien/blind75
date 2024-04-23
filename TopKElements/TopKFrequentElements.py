'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        frequency = {nums[0] : 1}
        
        for i in range(1, len(nums)):
            if frequency.get(nums[i]) is not None:
                frequency[nums[i]] += 1
            else:
                frequency[nums[i]] = 1
                
        print('frequency: '+ str(frequency))
                
        for num, frequency in frequency.items():
            heapq.heappush(heap, (frequency, num))
            if len(heap) > k:
                heapq.heappop(heap)
                
        top_k_elements = []
        
        while heap:
            top_k_elements.append(heapq.heappop(heap)[1])
            
        return top_k_elements
        
