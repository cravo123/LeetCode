# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    def __init__(self, root):
        self.q = []
        self.push(root)
        
    def push(self, node):
        while node:
            self.q.append(node)
            node = node.left
    
    def next(self):
        """
        @return the next smallest number
        """
        node = self.q.pop()
        res = node.val
        
        p = node.right
        self.push(p)
        
        return res