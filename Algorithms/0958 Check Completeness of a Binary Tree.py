# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        seen_none = False
        
        q = collections.deque([root])
        
        while q:
            p = q.popleft()
            if seen_none and p:
                return False
            if p is None:
                seen_none = True
            else:
                q.append(p.left)
                q.append(p.right)
        return True