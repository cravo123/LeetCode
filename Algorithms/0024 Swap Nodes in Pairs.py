# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1, simulation
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = curr = ListNode(None)
        dummy.next = head
        
        while curr.next and curr.next.next:
            first = curr.next
            second = curr.next.next
            tmp = curr.next.next.next
            
            curr.next = second
            second.next = first
            first.next = tmp
            
            curr = first
        
        return dummy.next