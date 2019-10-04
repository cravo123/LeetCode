# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1, fast and slow pointers, reverse linked list techniques
class Solution:
    def cut_half(self, node):
        slow = fast = node
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        # make sure to null first half tail
        prev.next = None
        
        prev, curr = None, slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp
        
        return node, prev
        
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head
        
        # cut in half
        p, q = self.cut_half(head)
        
        # paste half lists
        dummy = curr = ListNode(0)
        while p or q:
            if p:
                curr.next = p
                curr = curr.next
                p = p.next
            if q:
                curr.next = q
                curr = curr.next
                q = q.next
        
        return dummy.next
        
            
        
        
        