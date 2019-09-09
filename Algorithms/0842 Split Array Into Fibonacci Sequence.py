# Solution 1, Brute-Force + Back-tracking for recording paths
class Solution:
    def dfs(self, idx, S, path, res):
        if idx == len(S):
            if len(path) > 2:
                res.append(path[::])
            return
        need = sum(path[-2:])
        if need > 2 ** 31 - 1:
            return
        need = str(need)
        if S[idx:(idx + len(need))] == need:
            path.append(int(need))
            self.dfs(idx + len(need), S, path, res)
            path.pop()
        
    def splitIntoFibonacci(self, S: str) -> List[int]:
        path = []
        res = []
        
        n = len(S)
        
        for i in range(1, n - 1):
            for j in range(1, n - i):
                if i > 1 and S[0] == '0':
                    continue
                if j > 1 and S[i] == '0':
                    continue
                first = int(S[:i])
                second = int(S[i:(i + j)])
                
                if first > 2 ** 31 - 1 or second > 2 ** 31 - 1:
                    continue
                
                path.append(first)
                path.append(second)
                self.dfs(i + j, S, path, res)
                path.pop()
                path.pop()
        return res[0] if res else []
                