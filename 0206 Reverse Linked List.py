# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Iteration
class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        pre, curr = None, head
        
        while curr:
            p = curr.next
            curr.next = pre
            pre = curr
            curr = p
        return pre

# Recursion
class Solution:
    def reverse_helper(self, node):
        if node is None:
            return None, None
        
        if node.next is None:
            return node, node
        
        tail, head = self.reverse_helper(node.next)
        tail.next = node
        node.next = None
        
        return node, head
        
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        
        tail, head = self.reverse_helper(head)
        
        return head