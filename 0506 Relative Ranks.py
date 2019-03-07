class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        scores = [[c, i] for i, c in enumerate(nums)]
        scores.sort(reverse=True)
        
        scores = {v[0]:str(i + 1) for i, v in enumerate(scores)}
        
        res = [scores[x] for x in nums]
        
        for i in range(len(res)):
            if res[i] == '1':
                res[i] = 'Gold Medal'
            elif res[i] == '2':
                res[i] = 'Silver Medal'
            elif res[i] == '3':
                res[i] = 'Bronze Medal'
        return res