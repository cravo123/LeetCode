# Solution 1, DFS
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queens = set(tuple(queen) for queen in queens)
        
        q = []
        i, j = king
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == dj == 0:
                    continue
                x, y = i + di, j + dj
            
                if 0 <= x < 8 and 0 <= y < 8:
                    q.append([x, y, di, dj])
        
        res = []
        while q:
            i, j, di, dj = q.pop()
            if (i, j) in queens:
                res.append([i, j])
                queens.discard((i, j))
            else:
                x, y = i + di, j + dj
                if 0 <= x < 8 and 0 <= y < 8:
                    q.append([x, y, di, dj])
        
        return res