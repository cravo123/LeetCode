# Solution 1, simulation
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(nums), len(nums[0]) if nums else 0
        
        if m * n != r * c:
            return nums
        
        res = [[0 for _ in range(c)] for _ in range(r)]
        
        idx = 0
        for i in range(m):
            for j in range(n):
                res[idx // c][idx % c] = nums[i][j]
                idx += 1
        
        return res