# Solution 1, memoization, almost TLE
class Solution(object):
    def dfs(self, i, N, seen, d):
        if (i, N) in seen:
            return seen[i, N]
        
        if N == 1:
            return 1
        
        res = 0
        for j in d[i]:
            res += self.dfs(j, N - 1, seen, d)
        
        seen[i, N] = res
        
        return res
        
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        d = {}
        d[1] = [6, 8]
        d[2] = [7, 9]
        d[3] = [4, 8]
        d[4] = [3, 9, 0]
        d[5] = []
        d[6] = [1, 7, 0]
        d[7] = [2, 6]
        d[8] = [1, 3]
        d[9] = [2, 4]
        d[0] = [4, 6]
        
        res = 0
        seen = {}
        for i in range(10):
            res += self.dfs(i, N, seen, d)
        
        return res % int(10 ** 9 + 7)

# Solution 2, optimized memoization
# Loop N instead
class Solution:
    def dfs(self, i, N, seen, d):
        if (i, N) in seen:
            return seen[i, N]
        
        if N == 1:
            return 1
        
        res = 0
        for j in d[i]:
            res += self.dfs(j, N - 1, seen, d)
        
        res = res % int(10 ** 9 + 7)
        
        seen[i, N] = res
        
        return res
        
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        d = {}
        d[1] = [6, 8]
        d[2] = [7, 9]
        d[3] = [4, 8]
        d[4] = [3, 9, 0]
        d[5] = []
        d[6] = [1, 7, 0]
        d[7] = [2, 6]
        d[8] = [1, 3]
        d[9] = [2, 4]
        d[0] = [4, 6]

        q = [1 for _ in range(10)]
        
        for _ in range(N - 1):
            t = [0 for _ in range(10)]
            for i in range(10):
                for j in d[i]:
                    t[i] += q[j]
            q = [x % int(10 ** 9 + 7) for x in t]
            
        return sum(q) % int(10 ** 9 + 7)