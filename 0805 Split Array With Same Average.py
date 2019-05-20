# Solution 1, 0-1 knapsack DP



# Solution 2, enumerate, TLE
class Solution:
    def dfs(self, idx, A, path):
        if 0 < len(path) < len(A) and sum(A) == sum(path) * len(A) / len(path):
            return True
        
        for i in range(idx, len(A)):
            path.append(A[i])
            if self.dfs(i + 1, A, path):
                path.pop()
                return True
            path.pop()
        
        return False
        
    def splitArraySameAverage(self, A: List[int]) -> bool:
        if len(A) < 2:
            return False
        
        path = []
        
        return self.dfs(0, A, path)