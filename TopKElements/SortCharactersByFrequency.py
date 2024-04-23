'''
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.
'''

class Solution:
    def frequencySort(self, s: str) -> str:
        
        heap = []
        frequency = {}
        
        for i in s:
            if i not in frequency:
                frequency[i] = 0
            frequency[i] += 1
                    
        for character, frequency in frequency.items():
            heapq.heappush(heap, (-frequency, character))
            
        string = ""
        
        while heap:
            (frequency, character) = heapq.heappop(heap)
            for _ in range(-frequency):
                string += character
            
        return string
