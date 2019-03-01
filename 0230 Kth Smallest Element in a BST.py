# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def push(self, node):
        while node:
            self.q.append(node)
            node = node.left
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.q = []
        self.push(root)
        
        while k > 0:
            p = self.q.pop()
            res = p.val
            k -= 1
            p = p.right
            self.push(p)
        return res