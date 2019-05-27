import collections

# Solution 1, back-tracking
class Solution:
    def dfs(self, path, A, seen):
        if len(path) == len(A):
            self.res += 1
            return
        
        for i in range(len(A)):
            # Skip duplicate
            if i > 0 and A[i] == A[i - 1] and seen[i - 1] is False:
                continue
            if seen[i] is False:
                if not path or int(int((path[-1] + A[i]) ** 0.5 ) ** 2) == path[-1] + A[i]:
                    path.append(A[i])
                    seen[i] = True
                    self.dfs(path, A, seen)
                    seen[i] = False
                    path.pop()
                    
    def numSquarefulPerms(self, A: List[int]) -> int:
        path = []
        self.res = 0
        seen = [False for _ in A]
        A.sort()
        self.dfs(path, A, seen)
        
        return self.res

# Solution 1.1, same back-tracking 
# But pre-cache (A[i], A[j]) pairs that are squareful
class Solution:
    def dfs(self, c, cnt, d, cans):
        if cnt == 0:
            self.res += 1
            return
        
        d[c] -= 1
        for v in cans[c]:
            if d[v] > 0:
                self.dfs(v, cnt - 1, d, cans)
        d[c] += 1
        
    def numSquarefulPerms(self, A: List[int]) -> int:
        d = collections.Counter(A)
        
        cans = collections.defaultdict(set)
        
        for c1 in d:
            for c2 in d:
                if int(int((c1 + c2) ** 0.5) ** 2) == c1 + c2:
                    cans[c1].add(c2)
                    cans[c2].add(c1)
        
        self.res = 0
        n = len(A)
        
        for c in d:
            self.dfs(c, n - 1, d, cans)
        
        return self.res