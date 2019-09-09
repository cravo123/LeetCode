# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1, create dummy head
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = curr = ListNode(0)
        curr.next = head
        
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return dummy.next