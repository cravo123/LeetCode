class Solution:
    def dfs(self, i, prev, curr, num):
        if len(prev) > 1 and prev[0] == '0' or len(curr) > 1 and curr[0] == '0':
            return False
        n = len(num)
        if i >= n:
            return False
        
        new_val = str(int(prev) + int(curr))
        if num[i:] == new_val:
            return True
        if num[i:(i + len(new_val))] != new_val:
            return False
        
        return self.dfs(i + len(new_val), curr, new_val, num)
        
        
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        for i in range(n):
            for j in range(i):
                if self.dfs(i + 1, num[:(j + 1)], num[(j + 1):(i + 1)], num):
                    return True
        
        return False