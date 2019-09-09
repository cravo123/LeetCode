# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, inorder, postorder, in_i, in_j, post_i, post_j):
        if in_i >= in_j:
            return 
        
        root = TreeNode(postorder[post_j - 1])
        
        idx = inorder.index(postorder[post_j - 1])
        
        root.left = self.dfs(inorder, postorder, in_i, idx, post_i, post_i + idx - in_i)
        root.right = self.dfs(inorder, postorder, idx + 1, in_j, post_i + idx - in_i, post_j - 1)
        
        return root
        
        
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        res = self.dfs(inorder, postorder, 0, len(inorder), 0, len(postorder))
        
        return res