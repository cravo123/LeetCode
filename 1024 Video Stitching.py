# Solution 1, DP
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        dp = [-1 for _ in range(T + 1)]
        
        for s, e in clips:
            if s <= T:
                dp[s] = min(max(dp[s], e), T)
        
        left = right = 0
        
        steps = 0
        while True:
            t = -1
            for i in range(left, right + 1):
                t = max(t, dp[i])
            if t == -1:
                return -1
            if t >= T:
                return steps + 1
            left, right = right + 1, t
            steps += 1

# Solution 2, BFS
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        dp = [-1 for _ in range(T + 1)]
        
        for start, end in clips:
            if start <= T:
                dp[start] = max(dp[start], end)
        
        left = right = 0
        steps = 0
        
        while left <= right:
            if left <= T <= right:
                return steps
            tmp_right = right
            
            for i in range(left, right + 1):
                if dp[i] == -1:
                    continue
                tmp_right = max(tmp_right, dp[i])
            
            if tmp_right == right:
                return -1
            left, right = right + 1, tmp_right
            steps += 1
        return -1

