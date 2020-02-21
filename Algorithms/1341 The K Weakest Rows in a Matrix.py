# Solution 1, O(max(m * n, m * log m))
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        q = []
        
        for i in range(len(mat)):
            q.append([mat[i].count(1), i])
        
        q.sort()
        
        res = [idx for _, idx in q[:k]]
        
        return res

# Solution 2, binary search
class Solution:
    def count(self, row):
        n = len(row)
        
        # Find last 1
        i, j = 0, n
        while i < j:
            m = (i + j) // 2
            if row[m] == 1:
                i = m + 1
            else:
                j = m
        return j
        
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        q = []
        
        for i, row in enumerate(mat):
            cnt = self.count(row)
            heapq.heappush(q, [-cnt, -i])
            if len(q) > k:
                heapq.heappop(q)
        
        res = []
        while q:
            _, idx = heapq.heappop(q)
            res.append(-idx)
        
        return res[::-1]