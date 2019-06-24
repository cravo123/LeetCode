# Solution 1, Sweeping Line
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        q = []
        
        for cnt, start, end in trips:
            q.append([start, cnt])
            q.append([end, -cnt])
        
        q.sort()
        
        curr = 0
        
        for _, cnt in q:
            curr += cnt
            if curr > capacity:
                return False
        return True

# Solution 2, Counting sort-like
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = max(v for _, _, v in trips)
        
        q = [0 for _ in range(n + 1)]
        
        for cnt, start, end in trips:
            q[start] += cnt
            q[end] -= cnt
        
        curr = 0
        for cnt in q:
            curr += cnt
            if curr > capacity:
                return False
        return True