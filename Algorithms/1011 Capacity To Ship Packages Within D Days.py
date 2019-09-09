# Solution 1, Binary Search on Range, 
# same as LC 0875 Koko Eating Bananas
class Solution:
    def count_days(self, capacity, weights):
        res = 0
        curr = 0
        for w in weights:
            if w > capacity:
                return float('inf')
            if curr + w > capacity:
                res += 1
                curr = w
            else:
                curr += w
        res += 1
        return res
        
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = 1, sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            v = self.count_days(mid, weights)
            if v <= D:
                right = mid
            else:
                left = mid + 1
        return left