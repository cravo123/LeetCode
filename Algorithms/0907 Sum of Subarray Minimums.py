# Solution 1, Stack
class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        res = 0
        q = []
        A = [0] + A + [0]
        for i, c in enumerate(A):
            while q and A[q[-1]] > c:
                j = q.pop()
                res += (i - j) * (j - q[-1]) * A[j]
            q.append(i)
        
        return res % int(1e9 + 7)

# Solution 1.1, decompose to Previous Less Element and Next Less Element
# We need to take care of cases when element values are the same
# say, 2, 2, 2, 2, 1, 1, 2, 2
# This implementation makes sure that, 
#   NLE is the strict less value element
#   PLE is less or equal to value element
# NLE and PLE cannot both be less than or equal to, otherwise it will
# include duplicate results. 
class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        # Previous Less Element, Next Less Element
        n = len(A)
        PLE = [(i - 1) for i in range(n)]
        NLE = [n for i in range(n)]
        
        q = []
        
        for i, c in enumerate(A):
            while q and A[q[-1]] > c: # actually both > and >= would work
                j = q.pop()
                NLE[j] = i
            PLE[i] = q[-1] if q else -1
            q.append(i)
        
        res = 0
        BASE = int(1e9 + 7)
        
        for i in range(n):
            res += (i - PLE[i]) * (NLE[i] - i) * A[i]
        
        return res % BASE