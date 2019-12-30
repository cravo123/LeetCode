# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, level traversal
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        curr = [root]
        prev = []
        
        while curr:
            next_lvl = [q for p in curr for q in [p.left, p.right] if q]
            
            curr, prev = next_lvl, curr
        
        return sum(p.val for p in prev)
        