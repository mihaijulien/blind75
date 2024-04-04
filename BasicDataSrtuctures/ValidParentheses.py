class Solution:
    def is_valid(self, s: str) -> bool:

        parantheses = []

        for c in s:
            if c == '(' or c == '[' or c == '{':
                parantheses.append(c)
            elif c == ')' :
                if len(parantheses) != 0 and parantheses[-1] == '(':
                    parantheses.pop()
                else:
                    return False
            elif c == ']': 
                if len(parantheses) != 0 and parantheses[-1] == '[':
                    parantheses.pop()
                else:
                    return False
            elif c == '}' :
                if len(parantheses) != 0 and parantheses[-1] == '{':
                    parantheses.pop()
                else:
                    return False

        return len(parantheses) == 0
