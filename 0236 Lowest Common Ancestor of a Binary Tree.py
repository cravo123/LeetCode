# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursion
class Solution:
    def dfs(self, node, p, q):
        if node is None or node is p or node is q:
            return node
        L, R = self.dfs(node.left, p, q), self.dfs(node.right, p, q)
        if L is None:
            return R
        if R is None:
            return L
        return node
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.dfs(root, p, q)

# Iteration
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parent = {root: None}
        
        curr = [root]
        
        while p not in parent or q not in parent:
            node = curr.pop()
            if node is None:
                continue
            if node.left:
                parent[node.left] = node
            if node.right:
                parent[node.right] = node
            curr.append(node.left)
            curr.append(node.right)
        
        seen = set()
        while p:
            seen.add(p)
            p = parent[p]
        
        while q not in seen:
            q = parent[q]
        return q
