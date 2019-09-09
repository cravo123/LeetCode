# Solution 1, Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, cnt = None, 0
        
        for c in nums:
            if cnt == 0:
                res = c
            
            cnt += 1 if res == c else -1
        
        return res