# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        idx = 0
        
        while idx <= n:
            fast = fast.next
            idx += 1
        
        slow = dummy
        
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        
        return dummy.next