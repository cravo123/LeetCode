# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, recursion
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        
        return t1

# Solution 2, iteration
class Solution:
    def mergeTrees(self, t1: 'TreeNode', t2: 'TreeNode') -> 'TreeNode':
        q = [t1, t2]
        
        while q:
            p2, p1 = q.pop(), q.pop()
            if p1 is None or p2 is None:
                break
            p1.val += p2.val
            
            if p1.left is None or p2.left is None:
                if p1.left is None:
                    p1.left = p2.left
            else:
                q.append(p1.left)
                q.append(p2.left)
            
            if p1.right is None or p2.right is None:
                if p1.right is None:
                    p1.right = p2.right
            else:
                q.append(p1.right)
                q.append(p2.right)
        return t1 if t1 else t2
