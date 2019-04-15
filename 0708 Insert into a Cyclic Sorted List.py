"""
# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head is None:
            p = Node(insertVal, None)
            p.next = p
            return p
        
        curr = head
        
        while True:
            if (curr.val == insertVal
                or curr.val < insertVal < curr.next.val
                or (curr.val > curr.next.val and insertVal > curr.val)
                or (curr.val > curr.next.val and insertVal < curr.next.val)
                or curr.next is head):
                break
            curr = curr.next
        
        p = Node(insertVal, None)
        p.next = curr.next
        curr.next = p
                
        return head