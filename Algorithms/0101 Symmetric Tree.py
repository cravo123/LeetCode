# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, Recursion
class Solution:
    def dfs(self, p, q):
        if p is None or q is None:
            return p is q
        return p.val == q.val and self.dfs(p.left, q.right) and self.dfs(p.right, q.left)
        
    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        if root is None:
            return True
        return self.dfs(root.left, root.right)

# Solution 2, Iteration
class Solution:
    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        if root is None:
            return True
        
        q = [root.left, root.right]
        
        while q:
            R, L = q.pop(), q.pop()
            if L is None or R is None:
                if L is not R:
                    return False
                else:
                    continue
            if L.val != R.val:
                return False
            q.append(L.left)
            q.append(R.right)
            q.append(L.right)
            q.append(R.left)
        return True

# Solution 2.1, iteration using queue
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        q = [root]
        
        while q:
            t = [p.val if p else '#' for p in q]
            if t != t[::-1]:
                return False
            
            # remove none
            q = [p for p in q if p]
            q = [x for p in q for x in [p.left, p.right]]
        
        return True
