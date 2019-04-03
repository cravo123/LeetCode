# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

# Solution 1, return two values so we don't need a global res variable
class Solution:
    def dfs(self, node):
        if node is None:
            return 0, 0 # longest ending with curr node, curr longest length
        
        res = 1
        L, R = self.dfs(node.left), self.dfs(node.right)
        
        if node.left and node.left.val == node.val + 1:
            res = max(res, L[0] + 1)
        if node.right and node.right.val == node.val + 1:
            res = max(res, R[0] + 1)
        
        return res, max(res, L[1], R[1])
            
    def longestConsecutive(self, root: TreeNode) -> int:
        _, res = self.dfs(root)
        
        return res

# Solution 2, Using global variable
class Solution:
    def dfs(self, node):
        if node is None:
            return 0
        
        curr = 1
        L, R = self.dfs(node.left), self.dfs(node.right)
        
        if node.left and node.left.val == node.val + 1:
            curr = max(curr, L + 1)
        if node.right and node.right.val == node.val + 1:
            curr = max(curr, R + 1)
        self.res = max(self.res, curr)
        
        return curr
            
    def longestConsecutive(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root)
        
        return self.res

# Solution 3, Iterative, Breadth First Search
# Change queue to stack will become Depth First Search
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        q = collections.deque([[root, 1]])
        res = 0
        
        while q:
            node, curr = q.popleft()
            res = max(res, curr)
            
            for p in [node.left, node.right]:
                if p:
                    q.append([p, curr + 1 if p.val == node.val + 1 else 1])
        return res