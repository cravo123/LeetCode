class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        left, right = 0, n - 1
        res = 0
        
        # Left Boundary
        while left < right and seats[left] == 0:
            left += 1
        res = max(res, left)
        
        # Right Boundary
        while left < right and seats[right] == 0:
            right -= 1
        res = max(res, n - 1 - right)
        
        # Middle
        i = left
        curr = 0
        while i <= right:
            if seats[i] == 1:
                gap = i - curr
                res = max(res, gap // 2)
                curr = i
            i += 1
        
        return res