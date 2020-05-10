# Solution 1, simulation, memorize distance
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        curr = float('inf')
        
        for c in nums:
            if c == 1 and curr < k:
                return False
            
            if c == 1:
                curr = 0
            else:
                curr += 1
        
        return True

# Solution 1.1, simulation, memorize last 1's position