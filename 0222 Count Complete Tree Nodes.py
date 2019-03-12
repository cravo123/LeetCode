# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, only calculate left and right depth
class Solution:
    def left_depth(self, node):
        if node is None:
            return 0
        return 1 + self.left_depth(node.left)
    
    def right_depth(self, node):
        if node is None:
            return 0
        return 1 + self.right_depth(node.right)
    
    def countNodes(self, root: TreeNode) -> int:
        res = 0
        if root is None:
            return res
        
        L, R = self.left_depth(root), self.right_depth(root)
        if L == R:
            res += int(2 ** L - 1)
            return res
            
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# Solution 2, full-depth
class Solution:
    def depth(self, node):
        if node is None:
            return 0
        return 1 + max(self.depth(node.left), self.depth(node.right))
    
    def countNodes(self, root: TreeNode) -> int:
        res = 0
        node = root
        
        while node:
            L, R = self.depth(node.left), self.depth(node.right)
            if L == R:
                res += int(2 ** L)
                node = node.right
            else:
                res += int(2 ** R)
                node = node.left
        
        return res