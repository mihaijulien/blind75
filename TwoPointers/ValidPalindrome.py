'''
 Write a function that takes a string, s, as an input and determines whether or not it is a palindrome.

 Constraints:

    1 ≤ s.length ≤ 2×10^5
    The string s will contain English uppercase and lowercase letters, digits, and spaces.
'''
class Solution:
    def is_palindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] == s[right]:
                left = left + 1
                right = right - 1
            else:
                return False
        return True
