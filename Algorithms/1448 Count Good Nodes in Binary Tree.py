# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1, DFS recursion
class Solution:
    def dfs(self, node, curr_max):
        if node is None:
            return
        if node.val >= curr_max:
            self.res += 1
            curr_max = max(curr_max, node.val)
        self.dfs(node.left, curr_max)
        self.dfs(node.right, curr_max)
    
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        
        self.dfs(root, float('-inf'))
        
        return self.res

# Solution 2, DFS iteration
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = []
        
        if root:
            q.append([root, float('-inf')]) # [node, curr_max]
        
        while q:
            p, curr_max = q.pop()
            if p.val >= curr_max:
                res += 1
            curr_max = max(curr_max, p.val)
            
            if p.left:
                q.append([p.left, curr_max])
            
            if p.right:
                q.append([p.right, curr_max])
        
        return res