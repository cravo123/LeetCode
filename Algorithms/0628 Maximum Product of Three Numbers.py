from functools import reduce
import heapq

# Solution 1, O(nlogn)
# This is a sorting solution
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

# Solution 2,
# Since we only need to cache 3 largest numbers, and two smallest numbers
# heapq, or priority queue is a natural idea, O(nlog3) = O(n)
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        largest = heapq.nlargest(3, nums)
        smallest = heapq.nsmallest(2, nums)
        
        return max(reduce(lambda x, y: x * y, largest, 1), 
                   reduce(lambda x, y: x * y, smallest, 1) * largest[0])