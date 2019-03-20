"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def dfs(self, r_start, r_end, c_start, c_end, grid):
        v = grid[r_start][c_start]
        flag = True
        for i in range(r_start, r_end + 1):
            for j in range(c_start, c_end + 1):
                if grid[i][j] != v:
                    flag = False
                    break
        
        if flag:
            return Node(v, True, None, None, None, None)
        else:
            res = Node(None, False, None, None, None, None)
            r_mid = (r_start + r_end) // 2
            c_mid = (c_start + c_end) // 2
            res.topLeft = self.dfs(r_start, r_mid, c_start, c_mid, grid)
            res.topRight = self.dfs(r_start, r_mid, c_mid + 1, c_end, grid)
            res.bottomLeft = self.dfs(r_mid + 1, r_end, c_start, c_mid, grid)
            res.bottomRight = self.dfs(r_mid + 1, r_end, c_mid + 1, c_end, grid)
            
            return res
        
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        
        res = self.dfs(0, n - 1, 0, n - 1, grid)
        
        return res