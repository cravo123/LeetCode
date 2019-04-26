# Solution 1, Counting Sort
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        
        dp = [0 for _ in range(n + 1)]
        
        for c in citations:
            dp[min(c, n)] += 1
        
        j = n
        curr = dp[j]
        while j > 0 and j > curr:
            j -= 1
            curr += dp[j]
        
        return j