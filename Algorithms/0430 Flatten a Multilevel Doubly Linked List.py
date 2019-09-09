"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

# Solution 1, iteration
# Be careful when you link Double-Linked-List nodes
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        curr = head
        
        while curr:
            if curr.child:
                next_pt = curr.next
                curr.next = curr.child
                curr.next.prev = curr
                runner = curr.child
                curr.child = None
                
                while runner.next:
                    runner = runner.next
                runner.next = next_pt
                if next_pt:
                    next_pt.prev = runner
            curr = curr.next
        return head

# Solution 2, recursion, return two values, head and tail node
class Solution:
    def dfs(self, node):
        if node is None:
            return None, None
        
        if node.child is None and node.next is None:
            return node, node
        
        if node.child is None:
            head = node
            _, tail = self.dfs(node.next)
            return head, tail
        
        second = self.dfs(node.child)
        third = self.dfs(node.next)
        node.child = None
        
        head = node
        head.next = second[0]
        
        second[0].prev = head
        second[1].next = third[0]
        
        if third[0]:
            third[0].prev = second[1]
        
        if third[1]:
            tail = third[1]
        else:
            tail = second[1]
        
        return head, tail
        
    def flatten(self, head: 'Node') -> 'Node':
        
        res, _ = self.dfs(head)
        
        return res