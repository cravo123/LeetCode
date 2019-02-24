import collections

# Solution 1,
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        d = [0 for _ in range(N + 1)]
        
        for i, j in trust:
            d[i] -= 1
            d[j] += 1
            
        for i in range(1, N + 1):
            if d[i] == N - 1:
                return i
        return -1

# Solution 2,
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        judges = set(range(1, N + 1))
        d = collections.defaultdict(set)
        
        for a, b in trust:
            judges.discard(a)
            d[b].add(a)
        
        if len(judges) != 1:
            return -1
        res = judges.pop()
        if len(d[res]) != N - 1:
            return -1
        return res