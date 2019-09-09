# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node, path, res, target):
        if node is None:
            return
        
        if node.val == target and node.left is None and node.right is None:
            res.append(path + [node.val])
            return
        path.append(node.val)
        target -= node.val
        self.dfs(node.left, path, res, target)
        self.dfs(node.right, path, res, target)
        path.pop()
        
        
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        # typical back-tracking
        path = []
        res = []
        
        self.dfs(root, path, res, target)
        
        return res