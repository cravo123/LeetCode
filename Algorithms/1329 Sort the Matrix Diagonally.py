# Solution 1, simulation
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0]) if mat else 0
        
        for idx in range(m - 1, -n, -1):
            q = [mat[i][i - idx] for i in range(idx, m) if 0 <= i < m and 0 <= i - idx < n]
            # print(idx, q)
            q.sort()
            
            i = max(idx, 0)
            for c in q:
                mat[i][i - idx] = c
                i += 1
        
        return mat

# Solution 2, simulation, more straight-forward
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0]) if mat else 0
        
        d = collections.defaultdict(list)
        
        for i in range(m):
            for j in range(n):
                d[i - j].append(mat[i][j])
        
        for idx, vs in d.items():
            vs.sort(reverse=True)
            
        for i in range(m):
            for j in range(n):
                mat[i][j] = d[i - j].pop()
        
        return mat