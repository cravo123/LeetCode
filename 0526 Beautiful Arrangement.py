# Solution 1, back-tracking

class Solution:
    def dfs(self, idx, seen):
        if idx == len(seen):
            self.res += 1
            return
        
        for i in range(len(seen)):
            if seen[i]:
                continue
            if (i + 1) % (idx + 1) == 0 or (idx + 1) % (i + 1) == 0:
                seen[i] = True
                self.dfs(idx + 1, seen)
                seen[i] = False
        
    def countArrangement(self, N: int) -> int:
        self.res = 0
        seen = [False for _ in range(N)]
        
        self.dfs(0, seen)
        
        return self.res