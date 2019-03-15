# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        
        curr = head
        
        while curr:
            tmp = curr.next
            
            p = dummy
            while p.next and p.next.val < curr.val:
                p = p.next
            
            curr.next = p.next
            p.next = curr
            
            curr = tmp
        
        return dummy.next