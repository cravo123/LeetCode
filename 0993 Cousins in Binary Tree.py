# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, Recursion
class Solution:
    def calc(self, node, target, level):
        if node is None:
            return None, -1 # return parent node and level value
        
        if node.left and node.left.val == target:
            return node, level
        
        if node.right and node.right.val == target:
            return node, level
        
        level += 1
        L, R = self.calc(node.left, target, level), self.calc(node.right, target, level)
        
        if L[0]:
            return L
        
        if R[0]:
            return R
        
        return None, -1
        
    def isCousins(self, root: 'TreeNode', x: 'int', y: 'int') -> 'bool':
        
        first = self.calc(root, x, 0)
        second = self.calc(root, y, 0)
        
        return first[0] != second[0] and first[1] == second[1] and first[1] != -1

# Solution 2, iterative
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root is None or x == y:
            return False
        
        q = [root]
        
        while q:
            x_seen = y_seen = False
            
            tmp = []
            
            for p in q:
                if p.left and p.right:
                    if set([p.left.val, p.right.val]) == set([x, y]):
                        return False
                if p.left:
                    if p.left.val == x:
                        x_seen = True
                    elif p.left.val == y:
                        y_seen = True
                    tmp.append(p.left)
                if p.right:
                    if p.right.val == x:
                        x_seen = True
                    elif p.right.val == y:
                        y_seen = True
                    tmp.append(p.right)
            
            if x_seen and y_seen:
                return True
            
            q = tmp
        return False