import collections

# Solution 1,
# Mark the smallest available num that we can increment to
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        res = 0
        avail = 0
        
        for c in sorted(A):
            res += max(avail - c, 0)
            avail = max(avail + 1, c + 1)
        
        return res

# Solution 2, laze counting
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        unsolved = []
        
        d = collections.Counter(A)
        res = 0
        for c in range(int(1e5)):
            if d[c] > 1:
                unsolved.extend([c] * (d[c] - 1))
            elif d[c] == 0 and unsolved:
                res += c - unsolved.pop()
        
        return res

# Solution 3, simulation, TLE
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        d = collections.Counter(A)
        
        res = 0
        
        for c in A:
            if d[c] > 1:
                d[c] -= 1
                cnt = 0
                while c in d:
                    cnt += 1
                    c += 1
                d[c] += 1
                res += cnt
        return res