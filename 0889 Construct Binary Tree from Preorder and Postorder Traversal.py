# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, pre, post, pre_i, pre_j, post_i, post_j):
        if pre_i > pre_j:
            return
        if pre_i == pre_j:
            return TreeNode(pre[pre_i])
        root = TreeNode(pre[pre_i])
        
        pre_i += 1
        post_j -= 1
        
        val = post[post_j]
        idx = pre.index(val)
        
        root.left = self.dfs(pre, post, pre_i, idx - 1, post_i, post_i + idx - pre_i - 1)
        root.right = self.dfs(pre, post, idx, pre_j, post_i + idx - pre_i, post_j)
        
        return root
        
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        res = self.dfs(pre, post, 0, len(pre) - 1, 0, len(post) - 1)
        
        return res