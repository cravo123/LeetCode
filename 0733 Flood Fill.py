class Solution:
    def dfs(self, i, j, newColor, image, m, n):
        c = image[i][j]
        image[i][j] = newColor
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and image[x][y] == c:
                self.dfs(x, y, newColor, image, m, n)
        
    def floodFill(self, image: 'List[List[int]]', sr: 'int', sc: 'int', newColor: 'int') -> 'List[List[int]]':
        m, n = len(image), len(image[0]) if image else 0
        
        if image[sr][sc] == newColor:
            return image
        
        self.dfs(sr, sc, newColor, image, m, n)
        
        return image