import heapq

# Solution 1, priority queue
# First push first row to priority queue
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        
        q = [[matrix[0][j], 0, j] for j in range(n)]
        
        heapq.heapify(q)
        
        for _ in range(k):
            val, i, j = heapq.heappop(q)
            if i < n - 1:
                heapq.heappush(q, [matrix[i + 1][j], i + 1, j])
        return val

# Solution 2, Binary Search on Value Space
class Solution:
    def count(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        
        res = 0
        while i < m and j >= 0:
            if matrix[i][j] <= target:
                res += j + 1
                i += 1
            else:
                j -= 1
        return res
        
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left, right = matrix[0][0], matrix[-1][-1]
        
        while left < right:
            mid = (left + right) // 2
            cnt = self.count(matrix, mid)
            
            if cnt < k:
                left = mid + 1
            else:
                right = mid
        return left