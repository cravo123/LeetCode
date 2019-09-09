import heapq
# Solution 1, Best-First-Search, TLE
class Solution:
    def dist(self, i, j, end_i, end_j, forest, m, n):
        q = [[0, i, j]]
        seen = set([(i, j)])
        
        while q:
            curr, i, j = heapq.heappop(q)
            if (i, j) == (end_i, end_j):
                return curr
            
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and forest[x][y] > 0 and (x, y) not in seen:
                    seen.add((x, y))
                    heapq.heappush(q, [curr + 1, x, y])
        return -1
        
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0]) if forest else 0
        
        trees = []
        
        for i in range(m):
            for j in range(n):
                h = forest[i][j]
                if h > 1:
                    trees.append([h, i, j])
        trees.sort()
        
        res = 0
        prev_i, prev_j = 0, 0
        
        for _, curr_i, curr_j in trees:
            new_dist = self.dist(prev_i, prev_j, curr_i, curr_j, forest, m, n)
            if new_dist == -1:
                return -1
            res += new_dist
            prev_i, prev_j = curr_i, curr_j
        
        return res

# Solution 2, find detour distance, t.b.c
