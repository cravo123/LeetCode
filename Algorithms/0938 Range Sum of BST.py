# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, recursion
class Solution:
    def dfs(self, node, low, high):
        if node is None:
            return 0
        if node.val < low:
            return self.dfs(node.right, low, high)
        if node.val > high:
            return self.dfs(node.left, low, high)
        return node.val + self.dfs(node.left, low, high) + self.dfs(node.right, low, high)
    
    def rangeSumBST(self, root: 'TreeNode', L: 'int', R: 'int') -> 'int':
        return self.dfs(root, L, R)

# Solution 1, recursion using global variable
class Solution:
    def dfs(self, node, L, R):
        if node is None:
            return
        
        if L <= node.val <= R:
            self.res += node.val
        
        if node.val > L:
            self.dfs(node.left, L, R)
        if node.val < R:
            self.dfs(node.right, L, R)  
        
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.res = 0
        self.dfs(root, L, R)
        
        return self.res

# Solution 3, recursion without global variable
class Solution:
    def dfs(self, node, L, R):
        if node is None:
            return 0
        res = 0
        if L <= node.val <= R:
            res += node.val
        
        if node.val > L:
            res += self.dfs(node.left, L, R)
        if node.val < R:
            res += self.dfs(node.right, L, R)
        
        return res
        
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        return self.dfs(root, L, R)

# Solution 2, iteration
class Solution:
    def rangeSumBST(self, root: 'TreeNode', L: 'int', R: 'int') -> 'int':
        res = 0
        if root is None:
            return res
        
        q = [root]
        
        while q:
            p = q.pop()
            val = p.val
            
            if val < L and p.right:
                q.append(p.right)
            
            if val > R and p.left:
                q.append(p.left)
            
            if L <= val <= R:
                res += val
                if p.left:
                    q.append(p.left)
                if p.right:
                    q.append(p.right)
        return res