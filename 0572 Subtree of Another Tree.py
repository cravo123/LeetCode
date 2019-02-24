# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, Recursion
class Solution:
    def same(self, p, q):
        if p is None or q is None:
            return p is q
        return p.val == q.val and self.same(p.left, q.left) and self.same(p.right, q.right)
        
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None:
            return t is None
        return self.same(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

# Solution 2, we can pre-order traverse the tree, and remember null node as well,
# then to check if string_t is a substring of string_s
class Solution:
    def dfs(self, node, path):
        if node is None:
            path.append('#')
            return
        path.append(str(node.val))
        self.dfs(node.left, path)
        self.dfs(node.right, path)
        
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        path_s = ['']
        path_t = ['']
        
        self.dfs(s, path_s)
        self.dfs(t, path_t)
        
        s = ','.join(path_s)
        t = ','.join(path_t)
        
        return t in s
