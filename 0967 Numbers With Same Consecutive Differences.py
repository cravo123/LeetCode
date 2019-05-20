# Solution 1, back-tracking
# For problems that require enumerating all possible results,
# back-tracking is a typical solution.
class Solution:
    def dfs(self, N, K, path, res):
        if len(path) == N:
            res.append(int(''.join(str(x) for x in path)))
            return
        
        if not path:
            for i in range(1, 10):
                path.append(i)
                self.dfs(N, K, path, res)
                path.pop()
        else:
            for v in set([-K, K]):
                if 0 <= path[-1] + v <= 9:
                    path.append(path[-1] + v)
                    self.dfs(N, K, path, res)
                    path.pop()
        
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return list(range(10))
        
        res = []
        path = []
        
        self.dfs(N, K, path, res)
        
        return res

# Solution 2, iterative
# Start from 1 digit, iteratively adding more digits.
# t.b.c
