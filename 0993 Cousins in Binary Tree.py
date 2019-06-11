# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, Recursion
# Cache parent and level info
class Solution:
    def dfs(self, node, level, d, x, y):
        if node is None:
            return
        if node.left:
            if node.left.val == x:
                d[x] = [level + 1, node.val]
            if node.left.val == y:
                d[y] = [level + 1, node.val]
        if node.right:
            if node.right.val == x:
                d[x] = [level + 1, node.val]
            if node.right.val == y:
                d[y] = [level + 1, node.val]
        
        # prune
        if x in d and y in d:
            return
        
        level += 1
        self.dfs(node.left, level, d, x, y)
        self.dfs(node.right, level, d, x, y)
        
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        d = {}
        
        # Add dummy, so no need to special handling root
        dummy = TreeNode(None)
        dummy.left = root
        
        self.dfs(dummy, 0, d, x, y)
        
        if x == y or x not in d or y not in d:
            return False
        
        if d[x][0] != d[y][0]:
            return False
        
        if d[x][1] == d[y][1]:
            return False
        
        return True

# Solution 2, iterative
# BFS, early termination if we see x or y
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root is None:
            return False
        
        q = [root]
        
        while q:
            curr_vals = [x.val for p in q for x in [p.left, p.right] if x]
            
            is_x = x in curr_vals
            is_y = y in curr_vals
            
            if is_x or is_y:
                if not (is_x and is_y):
                    return False
                for p in q:
                    if p.left and p.right:
                        if set([p.left.val, p.right.val]) == set([x, y]):
                            return False
                return True
            
            q = [x for p in q for x in [p.left, p.right] if x]
        
        return False