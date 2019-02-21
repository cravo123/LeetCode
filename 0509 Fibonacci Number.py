class Solution:
    def fib(self, N: 'int') -> 'int':
        if N <= 1:
            return N
        idx = 1
        prev, curr = 0, 1
        
        while idx < N:
            prev, curr = curr, prev + curr
            idx += 1
        return curr
