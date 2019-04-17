# Solution 1, DP-like, but TLE, O(n!)
class Solution:
    def dfs(self, s):
        if s == '':
            return [s]
        
        res = []
        for i in range(len(s) + 1):
            if i == 0:
                c = s[0]
            else:
                c = str(i)
                
            for x in self.dfs(s[max(i, 1):]):
                if c.isdigit() and x and x[0].isdigit():
                    continue
                res.append(c + x)
        return res        
                
    def generateAbbreviations(self, word: str) -> List[str]:
        return self.dfs(word)

# Solution 2, back-tracking, O(2^n)
class Solution:
    def dfs(self, s, idx, cnt, path, res):
        if idx == len(s):
            res.append(''.join(path) + (str(cnt) if cnt > 0 else ''))
            return
        
        # not change s[idx]
        path.append(str(cnt) if cnt > 0 else '')
        path.append(s[idx])
        self.dfs(s, idx + 1, 0, path, res)
        path.pop()
        path.pop()
        
        # change s[idx]
        cnt += 1
        self.dfs(s, idx + 1, cnt, path, res)
        
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []
        path = []
        
        self.dfs(word, 0, 0, path, res)
        
        return res
