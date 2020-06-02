import heapq
# Solution 1, heap, O(N) to find largest number
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        
        a, b = heapq.heappop(nums), heapq.heappop(nums)
        
        return (- a - 1) * (- b - 1)