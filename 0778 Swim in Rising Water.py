import heapq

# Solution 1, BFS implemented by priority queue
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        q = [[grid[0][0], 0, 0]]
        seen = set([(0, 0)])
        
        res = 0
        
        while q:
            t, i, j = heapq.heappop(q)
            res = max(res, t)
            
            if (i, j) == (n - 1, n - 1):
                return res
            
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                x, y = i + di, j + dj
                if 0 <= x < n and 0 <= y < n and (x, y) not in seen:
                    heapq.heappush(q, [grid[x][y], x, y])
                    seen.add((x, y))
        return 

# Solution 2, binary search on value range
# t.b.cclass Solution:
    def tokenize(self, S):
        q = []
        
        i, n = 0, len(S)
        while i < n:
            if S[i] == ',':
                i += 1
            if S[i].isalpha():
                q.append([S[i]])
                i += 1
            else:
                tmp = []
                i += 1
                while i < n and S[i] != '}':
                    if S[i] == ',':
                        i += 1
                    else:
                        tmp.append(S[i])
                        i += 1
                q.append(tmp)
                i += 1
        return q
        
    def permute(self, S: str) -> List[str]:
        q = self.tokenize(S)
        
        res = [[]]
        
        for cs in q:
            res = [path + [c] for path in res for c in cs]
        
        res = [''.join(path) for path in res]
        res.sort()
        
        return res