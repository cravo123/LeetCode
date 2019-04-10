# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, parse string, and do recursion
class Solution:
    def dfs(self, s):
        if not s:
            return 
        
        # Get root node value
        curr = 0
        i = 0
        v = 1
        if s[i] == '-':
            v = -1
            i += 1
        while i < len(s) and (s[i].isdigit()):
            curr = curr * 10 + int(s[i])
            i += 1
        
        # Get left and right substring
        # balance is parenthese balance
        balance = 0
        j = i
        while j < len(s):
            if s[j] == '(':
                balance += 1
            elif s[j] == ')':
                balance -= 1
            if balance == 0:
                break
            j += 1
        
        root = TreeNode(curr * v)
        root.left = self.dfs(s[(i + 1):j])
        root.right = self.dfs(s[(j + 2):(len(s) - 1)])
        
        return root
        
    def str2tree(self, s: str) -> TreeNode:
        res = self.dfs(s)
        
        return res

# Solution 2, iterative with Stack
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        q = []
        i, n = 0, len(s)
        
        while i < n:
            if s[i] == '-' or s[i].isdigit():
                v = 1
                if s[i] == '-':
                    v = -1
                    i += 1
                curr = 0
                while i < n and s[i].isdigit():
                    curr = curr * 10 + int(s[i])
                    i += 1
                curr *= v
                t = TreeNode(curr)
                if q:
                    if q[-1].left:
                        q[-1].right = t
                    else:
                        q[-1].left = t
                q.append(t)
            elif s[i] == ')':
                q.pop()
                i += 1
            else:
                i += 1
        return q[-1] if q else None