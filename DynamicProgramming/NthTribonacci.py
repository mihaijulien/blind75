'''
Given a number n, calculate the corresponding Tribonacci number. The Tribonacci sequence TnTn​ is defined as:
T0=0, T1=1, T2=1, and  Tn+3= Tn + Tn+1 + Tn+2, for n>=0

The input number, n, is a non-negative integer.
'''

class Solution:
    def find_tribonacci(n: int) -> int:

        if n < 2:
            return n
        res = [1,1,2]
        print(res)
        for i in range(3, n):
            res.insert(i, res[i-3] + res[i-2] + res[i-1]) #at index i, insert that sum

        return res[n-1]
