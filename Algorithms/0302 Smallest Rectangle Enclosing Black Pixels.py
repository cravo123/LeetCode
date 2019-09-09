# Solution 1, DFS
class Solution:
    def dfs(self, i, j, image, m, n, seen):
        self.xl = min(self.xl, i)
        self.xr = max(self.xr, i)
        self.yu = min(self.yu, j)
        self.yd = max(self.yd, j)
        
        seen.add((i, j))
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and image[x][y] == '1' and (x, y) not in seen:
                self.dfs(x, y, image, m, n, seen)
        
        
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        
        m, n = len(image), len(image[0]) if image else 0
        
        self.xl = self.xr = x
        self.yu = self.yd = y
        seen = set()
        self.dfs(x, y, image, m, n, seen)
        
        return (self.xr - self.xl + 1) * (self.yd - self.yu + 1)

# Solution 2, Binary Search!
# Idea is that since there is only one black pixel block,
# then projected 1D area should be one continues interval
# so we can use binary search to determine boundary.
# t.b.c