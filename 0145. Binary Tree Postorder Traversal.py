# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion
class Solution:
    def dfs(self, node, res):
        if node is None:
            return
        self.dfs(node.left, res)
        self.dfs(node.right, res)
        res.append(node.val)
        
    def postorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        res = []
        self.dfs(root, res)
        return res

# Iteration 1
class Solution:
    def postorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        p, q = root, []
        
        res = []
        last = None
        
        while p or q:
            if p:
                q.append(p)
                p = p.left
            else:
                x = q[-1]
                if x.right and x.right is not last:
                    p = x.right
                else:
                    x = q.pop()
                    res.append(x.val)
                    last = x
        return res

# Iteration 2
# Traverse in Node -> Right -> Left, then reverse to be Left -> Right -> Node
class Solution:
    def postorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        res = []
        if root is None:
            return res
        q = [root]
        
        while q:
            p = q.pop()
            res.append(p.val)
            
            for x in [p.left, p.right]:
                if x:
                    q.append(x)
        return res[::-1]