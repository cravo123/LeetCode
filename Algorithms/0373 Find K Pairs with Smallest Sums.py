import heapq

# Solution 1, priority queue
# Similar to LC 0668 Kth Smallest Number in Multiplication Table
#       nums2   0                       1                       2
# nums1
# 0             nums1[0] + nums2[0],    nums1[0] + nums2[1],    nums1[0] + nums2[2]
# 1             nums1[1] + nums2[0],    nums1[1] + nums2[1],    nums1[1] + nums2[2]
# 2             nums1[2] + nums2[0],    nums1[2] + nums2[1],    nums1[2] + nums2[2]

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        m, n = map(len, (nums1, nums2))
        
        q = []
        for j in range(n):
            heapq.heappush(q, [nums1[0] + nums2[j], 0, j])
        
        res = []
        cnt = 0
        
        while q and cnt < k:
            v, i, j = heapq.heappop(q)
            res.append([nums1[i], nums2[j]])
            cnt += 1
            if i < m - 1:
                heapq.heappush(q, [nums1[i + 1] + nums2[j], i + 1, j])
            
        return res