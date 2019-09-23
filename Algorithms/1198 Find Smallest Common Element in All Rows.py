import collections
import heapq

# Solution 1, simulation using Set operations
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        d = set(mat[0])
        
        for row in mat:
            d &= set(row)
        
        res = list(sorted(d))
        return res[0] if res else -1

# Solution 2, simulation using iterator
# Use the fact that each row is sorted, so we maintain row iterator in q
# and also a counter of how many each value we have see so far
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0]) if mat else 0
        q = []
        d = collections.Counter()
        for i, row in enumerate(mat):
            q.append((row[0], i, 0)) # val, row, col
            d[row[0]] += 1
            
        heapq.heapify(q)
        
        while q:
            v, i, j = heapq.heappop(q)
            if d[v] != m:
                del d[v]
                j += 1
                if j == n:
                    return -1
                heapq.heappush(q, (mat[i][j], i, j))
                d[mat[i][j]] += 1
            else:
                return v