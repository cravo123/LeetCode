import bisect

# Solution 1, LIS, Longest Increasing Subsequence-Like
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        q = []
        
        for c in nums:
            idx = bisect.bisect_left(q, c)
            if idx < len(q):
                q[idx] = c
            else:
                q.append(c)
            
            if len(q) == 3:
                return True
        return False

# Solution 2, similar idea
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # a < b < c
        a = b = c = float('inf')
        
        for v in nums:
            if v in [a, b, c]:
                continue
            if v < a:
                a = v
            elif v < b:
                b = v
            elif v < c:
                c = v
        
        return True if c < float('inf') else False

# Solution 2.1
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = b = c = float('inf')
        
        for v in nums:
            if v <= a:
                a = v
            elif v <= b:
                b = v
            else:
                return True
        return False