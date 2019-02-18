# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: 'TreeNode') -> 'int':
        res = root.val
        
        q = [root]
        
        while q:
            tmp = []
            for p in q:
                for x in [p.left, p.right]:
                    if x:
                        tmp.append(x)
            
            if not tmp:
                break
            q = tmp
            
        return q[0].val