# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Merge Sort + Use fast and slow pointers to halve a linked list
class Solution:
    def merge(self, p, q):
        dummy = curr = ListNode(0)
        
        while p and q:
            if p.val < q.val:
                curr.next = p
                p = p.next
            else:
                curr.next = q
                q = q.next
            curr = curr.next
        if p:
            curr.next = p
        if q:
            curr.next = q
        return dummy.next
        
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        slow = fast = head
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None
        
        p, q = self.sortList(head), self.sortList(slow)
        
        return self.merge(p, q)
            