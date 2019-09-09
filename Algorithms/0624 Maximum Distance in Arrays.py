# Solution 1, brute-force enumerate all possibilities, O(n^2)
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        n = len(arrays)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                res = max(res, abs(arrays[i][0] - arrays[j][-1]))
        
        return res

# Solution 2, O(n)
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        n = len(arrays)
        curr_min, curr_max = arrays[0][0], arrays[0][-1]
        
        for i in range(1, n):
            res = max(res, arrays[i][-1] - curr_min)
            res = max(res, curr_max - arrays[i][0])
            
            curr_min = min(curr_min, arrays[i][0])
            curr_max = max(curr_max, arrays[i][-1])
        
        return res