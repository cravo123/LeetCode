import random
# Solution 1, reservoir sampling

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums        

    def pick(self, target: int) -> int:
        curr = 0
        res = 0
        
        for i, c in enumerate(self.nums):
            if c == target:
                curr += 1
                v = random.randrange(1, curr + 1)
                if v == 1:
                    res = i
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)