# Solution 1, if arr is a permutation of 0 to N - 1
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 0
        
        curr = float('-inf')
        
        for i, c in enumerate(arr):
            curr = max(curr, c)
            if curr == i:
                res += 1
        return res

# Solution 2, General Solution
class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        d = {}
        
        for i, c in enumerate(arr):
            d[c] = i
        
        res = 0
        curr = float('-inf')
        
        for i, c in enumerate(sorted(arr)):
            curr = max(curr, d[c])
            if curr == i:
                res += 1
        return res