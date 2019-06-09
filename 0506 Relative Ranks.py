# Solution 1, simulation
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        tmp = [[c, i] for i, c in enumerate(nums)]
        tmp.sort(reverse=True)
        
        res = nums[::]
        
        for i, (_, idx) in enumerate(tmp):
            if i > 2:
                res[idx] = str(i + 1)
            elif i == 2:
                res[idx] = 'Bronze Medal'
            elif i == 1:
                res[idx] = 'Silver Medal'
            else:
                res[idx] = 'Gold Medal'
        
        return res