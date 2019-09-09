# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, recursion
class Solution:
    def dfs(self, node):
        if node is None:
            return
        node.left, node.right = self.dfs(node.right), self.dfs(node.left)
        return node
    
    def invertTree(self, root: 'TreeNode') -> 'TreeNode':
        return self.dfs(root)

# Solution 2, iteration, preorder
# Idea is that we need to insert operations when doing traversing
# Here the operation we need to insert is to switch two children nodes(invert)
class Solution:
    def invertTree(self, root: 'TreeNode') -> 'TreeNode':
        if root is None:
            return root
        
        q = [root]
        
        while q:
            p = q.pop()
            
            p.left, p.right = p.right, p.left
            
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)
        return root

# Solution 2.1, iteration, inorder
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        p, q = root, []
        
        while p or q:
            if p:
                p.left, p.right = p.right, p.left
                q.append(p)
                p = p.left
            else:
                p = q.pop()
                p = p.right
        return root
