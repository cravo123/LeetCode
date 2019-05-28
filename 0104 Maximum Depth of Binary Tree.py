# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Similar to LC 0559 Maximum Depth of N-ary Tree
# Solution 1, recursion
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Solution 2, iteration
# Any type of traversal would work, 
# pre-order, in-order, post-order and level traversal

# Solution 2.1, level traversal
class Solution:
    def maxDepth(self, root: 'TreeNode') -> 'int':
        level = 0
        
        if root is None:
            return level
        
        q = [root]
        
        while q:
            level += 1
            q = [x for p in q for x in [p.left, p.right] if x]
        
        return level

# Solution 2.2, pre-order traversal
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        res = 0
        if root is None:
            return res
        
        q = [[root, 1]]
        
        while q:
            p, h = q.pop()
            res = max(res, h)
            
            h += 1
            if p.right:
                q.append([p.right, h])
            if p.left:
                q.append([p.left, h])
        
        return res