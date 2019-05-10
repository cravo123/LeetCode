# By Chong Chen, https://github.com/cravo123/LeetCode

# Solution 1, recursion
class Solution:
    def dfs(self, n):
        if n == 0:
            return 0
        if n <= 3:
            return 1
        return n - (n - 1) * (n - 2) // (n - 3) + self.dfs(n - 4)
        
        
    def clumsy(self, N: int) -> int:
        if N == 1:
            return 1
        if N == 2:
            return 2
        if N == 3:
            return 6
        return N * (N - 1) // (N - 2) + self.dfs(N - 3) 