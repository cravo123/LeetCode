import collections

# Solution 1, simulation
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        d = collections.Counter(nums)
        
        for v in sorted(d):          
            cnt = d[v]
            if cnt > 0:
                for inc in range(k):
                    d[v + inc] -= cnt
                    if d[v + inc] < 0:
                        return False
        return True