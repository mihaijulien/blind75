'''
You are given a string consisting of lowercase English letters. Repeatedly remove adjacent duplicate letters, one pair at a time. Both members of a pair of adjacent duplicate letters need to be removed.
'''

class Solution:
    def remove_duplicates(string: str) -> str:
        stack = []
        for c in string:
            if len(stack) == 0:
                stack.append(c)
            elif len(stack) != 0 and stack[-1] != c:
                stack.append(c)
            elif len(stack) != 0 and stack[-1] == c:
                stack.pop()

        return ''.join(stack)
