# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, Recursion
class Solution:
    def dfs(self, node, V):
        if node is None:
            return [None, None]
        
        if node.val == V:
            large = node.right
            node.right = None
            return [node, large]
        elif node.val <= V:
            small, large = self.dfs(node.right, V)
            node.right = small
            return [node, large]
        else:
            small, large = self.dfs(node.left, V)
            node.left = large
            return [small, node]
        
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
        return self.dfs(root, V)

# Solution 2, slightly succinct
class Solution:
    def dfs(self, node, V):
        if node is None:
            return [None, None]
        
        if node.val <= V:
            small, large = self.dfs(node.right, V)
            node.right = small
            return [node, large]
        else:
            small, large = self.dfs(node.left, V)
            node.left = large
            return [small, node]
        
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
        return self.dfs(root, V)