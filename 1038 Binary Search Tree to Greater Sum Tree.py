# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# This question is similar to LC 538 Convert BST to Greater Tree

# Solution 1, Iterative,
# Reverse In-order traversal, R -> N -> L
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        curr_sum = 0
        p, q = root, []
        
        while p or q:
            if p:
                q.append(p)
                p = p.right
            else:
                p = q.pop()
                p.val = curr_sum + p.val
                curr_sum = p.val
                p = p.left
        
        return root

# Solution 2, Recursion with global variable
# Easy to implement, but we need a global variable
# which might not be acceptable for some interviewer
class Solution:
    curr_sum = 0
    
    def dfs(self, node):
        if node is None:
            return
        self.dfs(node.right)
        node.val += self.curr_sum
        self.curr_sum = node.val
        self.dfs(node.left)
        
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.dfs(root)
        
        return root

# Solution 2.1, Recursion without global variable
# This is achieved through returning curr_sum
class Solution:
    def dfs(self, node, curr_sum):
        if node is None:
            return curr_sum
        curr_sum = self.dfs(node.right, curr_sum)
        node.val += curr_sum
        curr_sum = node.val
        
        return self.dfs(node.left, curr_sum)
        
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.dfs(root, 0)
        
        return root