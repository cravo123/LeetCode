"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""

# Solution 1, simulation
# first create and append copied node after each node
# then split the linked list
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return
        
        curr = head
        
        while curr:
            p = curr.next
            curr.next = Node(curr.val, p, None)
            curr = p
        
        curr = head
        dummy = res = Node(0, None, None)
        
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        curr = head
        while curr:
            res.next = curr.next
            res = res.next
            
            curr.next = curr.next.next
            curr = curr.next
        return dummy.next

# Solution 2, simulation using hashmap
