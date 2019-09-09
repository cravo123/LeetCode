class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        lens = [1 for _ in nums]
        cnts = [1 for _ in nums]
        
        res_len = 0
        res_cnt = 0
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lens[i] == lens[j] + 1:
                        cnts[i] += cnts[j]
                    elif lens[i] < lens[j] + 1:
                        cnts[i] = cnts[j]
                        lens[i] = lens[j] + 1
                    
            if lens[i] == res_len:
                res_cnt += cnts[i]
            elif lens[i] > res_len:
                res_cnt = cnts[i]
                res_len = lens[i]
                    
        return res_cnt