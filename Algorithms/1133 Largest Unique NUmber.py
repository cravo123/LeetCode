import collections

# Solution 1, sorting
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        A.sort(reverse=True)
        
        i, n = 0, len(A)
        
        while i < n:
            if (i == 0 or A[i] != A[i - 1]) and (i == n - 1 or A[i] != A[i + 1]):
                return A[i]
            i += 1
        
        return -1

# Solution 2, priority queue
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        d = collections.Counter(A)
        
        res = float('-inf')
        
        for c, v in d.items():
            if v == 1 and c > res:
                res = c
        
        return res if res > float('-inf') else -1