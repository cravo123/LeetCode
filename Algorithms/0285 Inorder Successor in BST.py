# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, iteration, maintain node that is larger than target
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        tail = None
        
        curr = root
        while curr:
            if curr.val <= p.val:
                curr = curr.right
            else:
                tail = curr
                curr = curr.left
        return tail

# Solution 2, recursion
class Solution:
    def dfs(self, node, target, tail):
        if node is None:
            return tail
        if node.val <= target.val:
            return self.dfs(node.right, target, tail)
        tail = node
        return self.dfs(node.left, target, tail)
        
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        tail = None
        
        res = self.dfs(root, p, tail)
        
        return res

# Solution 3, more elegant recursion
class Solution:
    def dfs(self, node, target):
        if node is None:
            return
        
        if node.val <= target.val:
            return self.dfs(node.right, target)
        
        res = self.dfs(node.left, target)
        
        return res or node
        
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        res = self.dfs(root, p)
        
        return res