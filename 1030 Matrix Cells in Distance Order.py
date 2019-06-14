import collections

# Solution 1, customized sort
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        res = [[i, j] for i in range(R) for j in range(C)]
        
        res.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
        
        return res

# Solution 2, BFS
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        q = collections.deque([[r0, c0]])
        seen = set()
        seen.add((r0, c0))
        
        res = []
        
        while q:
            i, j = q.popleft()
            res.append([i, j])
            
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                x, y = i + di, j + dj
                
                if 0 <= x < R and 0 <= y < C and (x, y) not in seen:
                    q.append([x, y])
                    seen.add((x, y))
        return res