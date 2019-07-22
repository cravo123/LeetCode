# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, in-order traversal iteration
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

# Solution 2, recursion
# function dfs returns how many node vals we have used
# so when k == 0, that is the result we need
class Solution:
    def dfs(self, node, k):
        if node is None:
            return k
        
        k = self.dfs(node.left, k)
        k -= 1
        if k == 0:
            self.res = node.val
        return self.dfs(node.right, k)
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.res = None
        self.dfs(root, k)
        
        return self.res