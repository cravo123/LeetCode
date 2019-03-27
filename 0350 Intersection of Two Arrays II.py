# Solution 1, hashmap, O(m + n) solution
import collections
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        d = collections.Counter(nums1)
        
        res = []
        
        for c in nums2:
            if d[c] > 0:
                res.append(c)
                d[c] -= 1
        
        return res

# Solution 2, follow-up, if nums1 and nums2 are sorted
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        m, n = map(len, (nums1, nums2))
        
        i = j = 0
        res = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        
        return res