# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, recursion, 
# kinda like post-order traversal in a sense that
# we deal with left and right children first, and then parent node
class Solution:
    def dfs(self, node, to_delete, res):
        if node is None:
            return
        
        L, R = self.dfs(node.left, to_delete, res), self.dfs(node.right, to_delete, res)
        
        if node.val in to_delete:
            if L:
                res.append(L)
            if R:
                res.append(R)
            
            return
        
        node.left, node.right = L, R
        
        return node
                
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res = []
        
        self.dfs(root, to_delete, res)
        
        if root and root.val not in to_delete:
            res.append(root)
        
        return res

# Solution 1.1, since we will change left and right child node in-place,
# the traversing order actually doesn't matter then.
class Solution:
    def dfs(self, node, is_add, to_delete, res):
        if node is None:
            return
        
        if node.val not in to_delete and is_add:
            res.append(node)
        
        is_add = node.val in to_delete
        node.left = self.dfs(node.left, is_add, to_delete, res)
        node.right = self.dfs(node.right, is_add, to_delete, res)
        
        return node if not is_add else None
        
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res = []
        
        self.dfs(root, True, to_delete, res)
        
        return res