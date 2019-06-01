# Solution 1, two-pointer

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = m + n - 1
        i, j = m - 1, n - 1
        
        while i >= 0 or j >= 0:
            v1 = nums1[i] if i >= 0 else float('-inf')
            v2 = nums2[j] if j >= 0 else float('-inf')
            
            if v1 >= v2:
                nums1[idx] = v1
                i -= 1
            else:
                nums1[idx] = v2
                j -= 1
            idx -= 1