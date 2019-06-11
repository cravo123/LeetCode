# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1, simulation
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1 = less = ListNode(0)
        dummy2 = more = ListNode(0)
        
        curr = head
        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                more.next = curr
                more = more.next
            curr = curr.next
        
        less.next = dummy2.next
        more.next = None
        
        return dummy1.next