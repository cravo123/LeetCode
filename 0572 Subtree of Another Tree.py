# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, Recursion
class Solution:
    def same(self, p, q):
        if p is None or q is None:
            return p is q
        return p.val == q.val and self.same(p.left, q.left) and self.same(p.right, q.right)
        
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None:
            return t is None
        return self.same(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

# Solution 2, we can pre-order traverse the tree, and remember null node as well,
# then to check if string_t is a substring of string_s
