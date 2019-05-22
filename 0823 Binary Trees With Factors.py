import collections

# Solution 1, Bottom-Up DP
class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        A.sort()
        d = collections.Counter()
        
        for i, c in enumerate(A):
            d[c] = 1
            for j in range(i):
                if A[i] % A[j] == 0 and A[i] // A[j] in d:
                    d[c] += d[A[j]] * d[A[i] // A[j]]
        
        return sum(d.values()) % int(1e9 + 7)

# Solution 2, Top-Down DP
class Solution:
    def dfs(self, c, A, d):
        if c not in A:
            return 0
        if c in d:
            return d[c]
        
        for i in A:
            if i > int(c ** 0.5):
                break
            if c % i == 0:
                first, second = i, c // i
                d[c] += self.dfs(first, A, d) * self.dfs(second, A, d) * (2 if first != second else 1)
        d[c] += 1
        return d[c]
        
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        A.sort()
        d = collections.Counter()
        
        for c in A:
            self.dfs(c, A, d)
        
        return sum(d.values()) % (int(1e9) + 7)