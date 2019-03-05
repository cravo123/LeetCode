# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = runner_1 = ListNode(0)
        even = runner_2 = ListNode(0)
        
        curr = head
        
        while curr:
            runner_1.next = curr
            runner_1 = runner_1.next
            curr = curr.next
            if curr:
                runner_2.next = curr
                runner_2 = runner_2.next
                curr = curr.next
        runner_1.next = even.next
        runner_2.next = None
        
        return odd.next