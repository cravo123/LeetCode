import collections
class Solution:
    def mark_1s(self, matrix):
        d = set()
        
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    d.add((i, j))
        
        return d
        
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        da, db = map(self.mark_1s, (A, B))
        
        d = collections.Counter()
        
        for i, j in da:
            for x, y in db:
                d[(x - i, y - j)] += 1
        if d:
            res = d.most_common(1)[0][1]
        else:
            res = 0
        
        return res