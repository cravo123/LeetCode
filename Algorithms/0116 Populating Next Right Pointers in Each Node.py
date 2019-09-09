"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# Solution 1
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        curr = root
        
        while curr and curr.left:
            next_level_node = runner = Node(0, None, None, None)
            
            while curr:
                runner.next = curr.left
                runner = runner.next
                runner.next = curr.right
                runner = runner.next
                
                curr = curr.next
            runner.next = None
            
            curr = next_level_node.next
        return root

# Solution 2, use the property that it is a complete tree
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        curr = root
        
        while curr:
            runner = curr
            while runner:
                if runner.left:
                    runner.left.next = runner.right
                    if runner.next:
                        runner.right.next = runner.next.left
                runner = runner.next
            curr = curr.left
        return root
