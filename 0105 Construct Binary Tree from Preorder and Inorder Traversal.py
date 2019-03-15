# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, preorder, pre_i, pre_j, inorder, in_i, in_j):
        if pre_i >= pre_j:
            return
        root = TreeNode(preorder[pre_i])
        
        idx = inorder.index(preorder[pre_i])
        cnt = idx - in_i
        
        root.left = self.dfs(preorder, pre_i + 1, pre_i + 1 + cnt, inorder, in_i, idx)
        root.right = self.dfs(preorder, pre_i + 1 + cnt, pre_j, inorder, idx + 1, in_j)
        
        return root
        
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        res = self.dfs(preorder, 0, len(preorder), inorder, 0, len(inorder))
        
        return res