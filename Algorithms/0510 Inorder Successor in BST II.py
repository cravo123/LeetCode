"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        # Case 1, node has right child
        if node.right:
            curr = node.right
            while curr.left:
                curr = curr.left
            return curr
        
        # Case 2, node has no right child, so needs to traverse
        # its parent
        curr = node
        prev = curr.parent
        
        while prev and prev.right is curr:
            curr, prev = prev, prev.parent
        
        return prev