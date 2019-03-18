# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less, more = ListNode(0), ListNode(0)
        runner_less = less
        runner_more = more
        
        curr = head
        
        while curr:
            if curr.val < x:
                runner_less.next = curr
                runner_less = runner_less.next
            else:
                runner_more.next = curr
                runner_more = runner_more.next
            curr = curr.next
        runner_less.next = more.next
        runner_more.next = None
        
        return less.next