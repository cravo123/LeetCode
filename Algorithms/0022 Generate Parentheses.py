# Solution 1, back-tracking
class Solution:
    def dfs(self, left, right, path, res, n):
        if left == right == n:
            res.append(''.join(path))
            return
        
        # we can always add '('
        if left < n:
            path.append('(')
            self.dfs(left + 1, right, path, res, n)
            path.pop()
        
        # if right < left, we can add ")"
        if right < left:
            path.append(')')
            self.dfs(left, right + 1, path, res, n)
            path.pop()
        
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        res = []
        
        self.dfs(0, 0, path, res, n)
        
        return res

# Solution 1.1, a more understandable back-tracking
class Solution:
    def dfs(self, left, right, path, res):
        if left > right:
            return
        if left == right == 0:
            res.append(''.join(path))
            return
        
        if left > 0:
            path.append('(')
            self.dfs(left - 1, right, path, res)
            path.pop()
        path.append(')')
        self.dfs(left, right - 1, path, res)
        path.pop()
        
        
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        res = []
        
        self.dfs(n, n, path, res)
        
        return res