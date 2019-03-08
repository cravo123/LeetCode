"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        curr = head
        
        while curr:
            if curr.child:
                next_node = curr.next
                runner = curr.child
                curr.child = None
                curr.next = runner
                runner.prev = curr
                
                while runner.next:
                    runner = runner.next
                
                runner.next = next_node
                if next_node:
                    next_node.prev = runner
            else:
                curr = curr.next
        
        return head