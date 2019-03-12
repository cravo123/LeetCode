# Solution 1, Top-Down
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        pre = [0]
        
        for row in triangle:
            curr = row[::]
            for i in range(len(row)):
                if i == 0:
                    curr[i] = row[i] + pre[i]
                elif i == len(row) - 1:
                    curr[i] = row[i] + pre[i - 1]
                else:
                    curr[i] = min(pre[i - 1], pre[i]) + row[i]
            pre = curr
        
        return min(pre)

# Solution 2, Bottom-up, less special case
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        
        res = triangle[-1][::]
        
        for j in range(len(triangle) - 2, -1, -1):
            row = triangle[j]
            for i in range(len(row)):
                res[i] = row[i] + min(res[i], res[i + 1])
    
        return res[0]