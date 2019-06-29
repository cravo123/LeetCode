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

# Solution 1, recursion
class Solution:
    def dfs(self, up, down, left, right, grid):
        v = grid[up][left]
        flag = True
        for i in range(up, down + 1):
            for j in range(left, right + 1):
                if grid[i][j] != v:
                    flag = False
                    break
        
        if flag:
            return Node(v, True, None, None, None, None)
        
        r_mid = (up + down) // 2
        c_mid = (left + right) // 2
        
        tl = self.dfs(up, r_mid, left, c_mid, grid)
        tr = self.dfs(up, r_mid, c_mid + 1, right, grid)
        bl = self.dfs(r_mid + 1, down, left, c_mid, grid)
        br = self.dfs(r_mid + 1, down, c_mid + 1, right, grid)
        
        return Node(None, False, tl, tr, bl, br)
        
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        
        return self.dfs(0, n - 1, 0, n - 1, grid)