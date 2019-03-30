# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Key point is to observe that there are three statuses for a node
# 0: covered by a camera
# 1: there is a camera at this node
# 2: this node is not covered by a camera, so its parent needs to have 
#    a camera

class Solution:
    def dfs(self, node):
        # return value
        # 0: covered
        # 1: camera at this node
        # 2: not covered
        if node is None:
            return 0
        L, R = self.dfs(node.left), self.dfs(node.right)
        
        if 2 in [L, R]:
            self.res += 1
            return 1
        
        if 1 in [L, R]:
            return 0
        
        return 2
        
    def minCameraCover(self, root: TreeNode) -> int:
        self.res = 0
        
        tag = self.dfs(root)
        
        return self.res if tag != 2 else self.res + 1