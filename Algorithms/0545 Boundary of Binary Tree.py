# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1, solve left_boundary, leaves, right_boundary separately
class Solution:
    def left_bound(self, node):
        q = []
        while node:
            if node.left is None and node.right is None:
                break
            q.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right
        return q
    
    def right_bound(self, node):
        q = []
        while node:
            if node.left is None and node.right is None:
                break
            q.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left
        return q
    
    def leaves(self, node, res):
        q = [node]
        
        while q:
            p = q.pop()
            if p.left is None and p.right is None:
                res.append(p.val)
            else:
                if p.right:
                    q.append(p.right)
                if p.left:
                    q.append(p.left)
        
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        res = []
        
        if root is None:
            return res
    
        res.append(root.val)
        if root.left is None and root.right is None:
            return res
        
        q_l = self.left_bound(root.left)
        res.extend(q_l)
        
        q = []
        self.leaves(root, q)
        res.extend(q)
        
        q_r = self.right_bound(root.right)
        res.extend(q_r[::-1])
        
        return res


# Solution 2, elegant recursion
class Solution:
    def dfs(self, node, is_left, is_right, res):
        if node is None:
            return
        
        if is_left:
            res.append(node.val)
        
        if is_left == is_right == False and node.left == node.right == None:
            res.append(node.val)
        
        self.dfs(node.left, is_left, is_right and node.right is None, res)
        self.dfs(node.right, is_left and node.left is None, is_right, res)
        
        if is_right:
            res.append(node.val)
        
    
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        res = []
        
        if root is None:
            return res
        
        res.append(root.val)
        
        self.dfs(root.left, True, False, res)
        self.dfs(root.right, False, True, res)
        
        return res