import heapq

# Solution 1, manual 'heap'
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')
        
        for c in nums:
            if c in [first, second, third]:
                continue
            
            if c > first:
                first, second, third = c, first, second
            elif c > second:
                second, third = c, second
            elif c > third:
                third = c
        
        return third if third > float('-inf') else first

# Solution 2, heapq
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        q = [float('-inf') for _ in range(3)]
        
        for c in nums:
            if c in q:
                continue
            heapq.heappush(q, c)
            heapq.heappop(q)
        
        res = heapq.heappop(q)
        heapq.heappop(q)
        first = heapq.heappop(q)
        
        return res if res > float('-inf') else first