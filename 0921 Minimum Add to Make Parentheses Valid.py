# Solution 1, O(n^2) LIS, longest Increasing Subsequence
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        curr = 0
        res = 0
        
        for c in S:
            if c == '(':
                curr += 1
            else:
                curr -= 1
            
            if curr < 0:
                res += 1
                curr = 0
        res += curr
        
        return res

# Solution 2, O(nlogn) binary search
# maintain invariant of tail, note dp[i] means the smallest tail value
# of length (i + 1)
import bisect
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