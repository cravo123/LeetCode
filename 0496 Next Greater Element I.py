# Longest Increasing Subsequence(LIS) idea
# the stack maintains an invariant of decreasing subsequence
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {c:-1 for c in nums1}
        
        q = []
        
        for c in nums2:
            while q and q[-1] < c:
                x = q.pop()
                if x in d:
                    d[x] = c
            q.append(c)
        
        res = [d[c] for c in nums1]
        
        return res