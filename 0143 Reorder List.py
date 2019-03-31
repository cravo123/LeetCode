# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def split(self, node):
        prev = None
        slow = fast = node
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if prev:
            prev.next = None
        
        return slow
    
    def reverse(self, node):
        prev, curr = None, node
        while curr:
            p = curr.next
            curr.next = prev
            prev = curr
            curr = p
        
        return prev
    
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # This special handling is important. 
        # Otherwise for single node, it will generate
        # circle linked list
        if head is None or head.next is None:
            return
        
        mid = self.split(head)
        h1 = head
        h2 = self.reverse(mid)
        dummy = curr = ListNode(0)
        
        while h1 and h2:
            t1, t2 = h1.next, h2.next
            curr.next = h1
            h1.next = h2
            curr = h2
            
            h1, h2 = t1, t2
        
        if h1:
            curr.next = h1
        
            
        
        
        