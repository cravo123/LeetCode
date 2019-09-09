# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        dummy = curr = ListNode(0)
        dummy.next = head
        
        while curr.next:
            if curr.next.next and curr.next.val == curr.next.next.val:
                runner = curr.next
                while runner and runner.val == curr.next.val:
                    runner = runner.next
                curr.next = runner
            else:
                curr = curr.next
        
        return dummy.next