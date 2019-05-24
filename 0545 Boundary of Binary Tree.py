# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        
        left, bottom, right = [], [], []
        
        # right boundary
        p = root.right 
        while p:
            right.append(p.val)
            if p.right:
                p = p.right
            else:
                p = p.left
        
        # left boundary
        p = root.left
        while p:
            left.append(p.val)
            if p.left:
                p = p.left
            else:
                p = p.right
        right.reverse()
        
        # bottom
        p, q = root, []
        while p or q:
            if p:
                q.append(p)
                p = p.left
            else:
                p = q.pop()
            
                if p.left is None and p.right is None:
                    bottom.append(p.val)
                
                p = p.right
        
        res = [root.val] + left[:-1] + bottom + right[1:]
        
        return res