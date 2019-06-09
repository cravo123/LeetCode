# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1, iteration
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        
        while curr:
            p = curr.next
            curr.next = prev
            prev, curr = curr, p
        
        return prev

# Solution 2, recursion
class Solution:
    def reverse_help(self, node):
        if node is None or node.next is None:
            return node, node # tail, head
        
        tail, head = self.reverse_help(node.next)
        tail.next = node
        node.next = None
        
        return node, head
        
    def reverseList(self, head: ListNode) -> ListNode:
        _, res = self.reverse_help(head)
        
        return res

# Solution 2.1, recursion
# Actually we only need to return one node, head 
