# Solution 1, moving forward
class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        d = {i: [x, y] for i, x, y in zip(indexes, sources, targets)}
        
        res = []
        i = 0
        n = len(S)
        
        while i < n:
            if i in d:
                old_str, new_str = d[i]
                if S[i:(i + len(old_str))] == old_str:
                    res.append(new_str)
                    i += len(old_str)
                    continue
            res.append(S[i])
            i += 1
        
        res = ''.join(res)
        
        return res

# Solution 2, moving backward, better solution 
class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        d = {i: [x, y] for i, x, y in zip(indexes, sources, targets)}
        
        n = len(S)
        i = n - 1
        S = list(S)
        
        while i >= 0:
            if i in d:
                old_str, new_str = d[i]
                if S[i:(i + len(old_str))] == list(old_str):
                    S[i:(i + len(old_str))] = list(new_str)
            i -= 1
        
        res = ''.join(S)
        
        return res