# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, iteration, we cache next level nodes first
# According to the problem, there are at most two nodes on each level

#       prev
#     /      \
#   curr     right
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        prev = None
        
        curr, right = root, None
        
        while curr:
            tmp, tmp_right = curr.left, curr.right
            
            curr.left = right
            curr.right = prev
            
            prev = curr
            curr, right = tmp, tmp_right
        
        return prev

# Solution 2, Recursion
class Solution:
    def dfs(self, node):
        if node is None or node.left is None:
            return node
        res = self.dfs(node.left)
        
        node.left.left = node.right
        node.left.right = node
        
        node.left = None
        node.right = None
        
        return res
        
        
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        res = self.dfs(root)
        
        return res
