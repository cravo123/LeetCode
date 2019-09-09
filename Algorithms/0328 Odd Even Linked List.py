# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1, simulation
# Similar to LC 0086 Partition List
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        dummy1 = odd = ListNode(None)
        dummy2 = even = ListNode(None)
        
        curr = head
        idx = 1
        
        while curr:
            if idx == 1:
                odd.next = curr
                odd = odd.next
            else:
                even.next = curr
                even = even.next
            curr = curr.next
            idx = 1 - idx
        
        odd.next = dummy2.next
        even.next = None
        
        return dummy1.next