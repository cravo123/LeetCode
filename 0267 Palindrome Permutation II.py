import collections

# Solution 1, back-tracking
class Solution:
    def dfs(self, cnt, d, path, res):
        if cnt == 0:
            res.append(''.join(path))
            return
        
        if cnt == 1:
            for c in d:
                if d[c] == 1:
                    path[len(path) // 2] = c
                    self.dfs(cnt - 1, d, path, res)
                    path[len(path) // 2] = ''
        else:
            for c in d:
                if d[c] > 1:
                    idx = (len(path) - cnt) // 2
                    path[idx] = path[len(path) - idx - 1] = c
                    d[c] -= 2
                    self.dfs(cnt - 2, d, path, res)
                    path[idx] = path[len(path) - idx - 1] = ''
                    d[c] += 2
            
    def generatePalindromes(self, s: str) -> List[str]:
        if not s:
            return ['']
        
        d = collections.Counter(s)
        
        if sum(1 for c in d if d[c] % 2 == 1) > 1:
            return []
        
        if len(s) % 2 == 0 and any(d[c] % 2 == 1 for c in d):
            return []
        
        res = []
        path = ['' for _ in s]
        
        self.dfs(len(s), d, path, res)
        
        return res

# Solution 2, same back-tracking idea
# But since this is palindrome, we only need to build half of the result!
# Similar to LC 0247
# t.b.c