import bisect

# Solution 1, DP, O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in nums]
        n = len(nums)
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp + [0]) # add [0] because dp could be empty

# Solution 2, O(nlogn) binary search
# maintain invariant of tail, note dp[i] means the smallest tail value
# of length (i + 1)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        q = []
        
        for c in nums:
            idx = bisect.bisect_left(q, c)
            if idx == len(q):
                q.append(c)
            else:
                q[idx] = c
            
        return len(q)