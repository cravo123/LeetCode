# Solution 1, DP, TLE
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = 0
        
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        
        return dp[-1]

# Solution 2, BFS, maximum level is 4
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        
        q = []
        i = 1
        
        while i * i <= n:
            q.append(i * i)
            i += 1
        
        if q[-1] == n:
            return 1
        
        curr = q[::]
        seen = set(curr)
        
        steps = 1
        while curr:
            tmp = []
            steps += 1
            for v in curr:
                for u in q:
                    if u + v == n:
                        return steps
                    if u + v not in seen:
                        seen.add(u + v)
                        tmp.append(u + v)
            curr = tmp