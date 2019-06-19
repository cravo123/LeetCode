import collections

# Solution 1, Brute-Force, O(n^2)
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        
        n = len(time)
        for i in range(1, n):
            for j in range(i):
                if (time[i] + time[j]) % 60 == 0:
                    res += 1
        
        return res

# Solution 2:
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = collections.Counter()
        
        for t in time:
            d[t % 60] += 1
        
        res = 0
        
        for t in sorted(d):
            if t == 0 or t == 30:
                res += ((d[t] - 1) * d[t]) // 2
            elif t > 30:
                break
            else:
                res += d[t] * d[60 - t]
        
        return res

# Solution 3, 
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = collections.Counter()
        res = 0
        
        for t in time:
            t = t % 60
            res += d[(60 - t) % 60]
            d[t] += 1
        
        return res