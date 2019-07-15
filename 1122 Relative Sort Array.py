import collections

# Solution 1, customized sorting
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {c:i for i, c in enumerate(arr2)}
        n = len(arr2)
        arr1.sort(key=lambda x: d.get(x, x + n)) # if not exist in arr2, use its own value to sort
        
        return arr1

# Solution 2, counting sort
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = collections.Counter(arr1)
        
        res = []
        
        for c in arr2:
            if c in d:
                res.extend([c] * d[c])
        
        arr2 = set(arr2)
        
        for c in range(1001):
            if c in d and c not in arr2:
                res.extend([c] * d[c])
        
        return res