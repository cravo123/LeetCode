# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1, simulation
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

# Solution 1.1, similar idea
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        
        fast = slow = dummy
        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        
        return dummy.next