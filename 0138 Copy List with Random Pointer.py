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
        
        # add copied node
        curr = head
        while curr:
            tmp = curr.next
            curr.next = Node(curr.val, tmp, None)
            curr = tmp
        
        # update random
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # split
        res = head.next
        p, q = head, head.next
        while p:
            p.next = q.next
            
            if q.next:
                q.next = q.next.next
            
            p = p.next
            q = q.next
        
        return res

# Solution 2, simulation using hashmap
