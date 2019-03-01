class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # Binary Search on Value Space
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            time = sum((num - 1) // mid + 1 for num in piles)
            
            if time > H:
                left = mid + 1
            else:
                right = mid
        
        return left