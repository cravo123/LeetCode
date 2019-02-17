# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion
class Solution:
    def dfs(self, node1, node2):
        if node1 is None:
            return node2
        if node2 is None:
            return node1
        node1.val += node2.val
        node1.left, node1.right = self.dfs(node1.left, node2.left), self.dfs(node1.right, node2.right)
        
        return node1
        
    def mergeTrees(self, t1: 'TreeNode', t2: 'TreeNode') -> 'TreeNode':
        return self.dfs(t1, t2)

# Iteration
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
