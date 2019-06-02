# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, BFS level traverse
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q = [root]
        
        while q:
            tmp = [x for p in q for x in [p.left, p.right] if x]
            if not tmp:
                break
            q = tmp
        
        return q[0].val

# Solution 2, DFS recursion
class Solution:
    def dfs(self, node, level, idx):
        if node is None:
            return
        
        if level > self.res[1] or level == self.res[1] and idx < self.res[2]:
            self.res = node, level, idx
        
        level += 1
        self.dfs(node.left, level, idx * 2)
        self.dfs(node.right, level, idx * 2 + 1)
        
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.res = root, 1, 1 # node, depth level, horizontal index
        
        self.dfs(root, 1, 1)
        
        return self.res[0].val
