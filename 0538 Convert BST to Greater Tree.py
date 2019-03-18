# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, similar to Solution 2, but with global var, 
# although simple, it is not elegant
class Solution:
    def dfs(self, node):
        if node is None:
            return
        self.dfs(node.right)
        
        node.val += self.curr
        self.curr = node.val
        
        self.dfs(node.left)
        
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.curr = 0
        
        self.dfs(root)
        
        return root


# Solution 2, similar to LC 530, minimum absolute difference in BST of returning prev
class Solution:
    def dfs(self, node, prev):
        if node is None:
            return prev
        prev = self.dfs(node.right, prev)
        
        node.val += prev
        
        prev = self.dfs(node.left, node.val)
        
        return prev
        
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.dfs(root, 0)
        
        return root

# Solution 3, in-order traverse, but in reverse-order, i.e. right -> curr -> left
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        prev = 0
        p, q = root, []
        
        while p or q:
            if p:
                q.append(p)
                p = p.right
            else:
                p = q.pop()
                p.val += prev
                prev = p.val
                p = p.left
        return root