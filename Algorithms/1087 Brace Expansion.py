# Solution 1, back-tracking, DFS
# Similar to LC 0017 Letter Combinations of a Phone Number
class Solution(object):
    def tokenize(self, S):
        q = []
        
        i, n = 0, len(S)
        while i < n:
            if S[i] == ',':
                i += 1
            elif S[i].isalpha():
                q.append([S[i]])
                i += 1
            else:
                tmp = []
                i += 1
                while i < n and S[i] != '}':
                    if S[i] == ',':
                        i += 1
                    else:
                        tmp.append(S[i])
                        i += 1
                q.append(tmp)
                i += 1
        return q
    
    def dfs(self, idx, q, path, res):
        if idx == len(q):
            res.append(''.join(path))
            return
        
        for c in q[idx]:
            path.append(c)
            self.dfs(idx + 1, q, path, res)
            path.pop()
    
    def expand(self, S: str) -> List[str]:
        q = self.tokenize(S)
        
        path = []
        res = []
        
        self.dfs(0, q, path, res)
        
        res.sort()
        
        return res

# Solution 2, iteration, BFS
#   step 1, tokenize string S to be list of list of strings
#   step 2, iterate through tokenized items, and append on the fly
class Solution:
    def tokenize(self, S):
        q = []
        
        i, n = 0, len(S)
        while i < n:
            if S[i] == ',':
                i += 1
            elif S[i].isalpha():
                q.append([S[i]])
                i += 1
            else:
                tmp = []
                i += 1
                while i < n and S[i] != '}':
                    if S[i] == ',':
                        i += 1
                    else:
                        tmp.append(S[i])
                        i += 1
                q.append(tmp)
                i += 1
        return q
        
    def expand(self, S: str) -> List[str]:
        q = self.tokenize(S)
        
        res = [[]]
        
        for cs in q:
            res = [path + [c] for path in res for c in cs]
        
        res = [''.join(path) for path in res]
        res.sort()
        
        return res