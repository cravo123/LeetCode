import collections

# Solution 1, dict + set
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        d = collections.Counter(nums1)
        cans = set(nums2)
        
        res = []
        
        for c in d:
            if c in cans:
                res.append(c)
        
        return res

# Solution 2, set + set
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set(nums1) & set(nums2)
        
        res = list(res)
        
        return res

# Solution 3, Sort + 2 Pointers
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        m, n = len(nums1), len(nums2)
        
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
                # Avoid duplicate results
                while i < m and nums1[i] == nums1[i - 1]:
                    i += 1
                
                while j < n and nums2[j] == nums2[j - 1]:
                    j += 1
        return res