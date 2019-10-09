import collections

# Solution 1, Counter
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        d1, d2, d3 = map(collections.Counter, (arr1, arr2, arr3))
        
        q = d1 & d2 & d3
        
        res = []
        
        for v, cnt in q.items():
            res.extend([v] * cnt)
        
        return res

# Solution 2, simulation using pointer
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        l1, l2, l3 = map(len, (arr1, arr2, arr3))
        i = j = k = 0
        res = []
        
        while i < l1 and j < l2 and k < l3:
            lo, hi = min(arr1[i], arr2[j], arr3[k]), max(arr1[i], arr2[j], arr3[k])
            
            if lo == hi:
                res.append(arr1[i])
                i += 1
                j += 1
                k += 1
            else:
                if arr1[i] < hi:
                    i += 1
                if arr2[j] < hi:
                    j += 1
                if arr3[k] < hi:
                    k += 1
        return res