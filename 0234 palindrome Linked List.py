# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, curr = None, slow
        
        while curr:
            p = curr.next
            curr.next = prev
            prev = curr
            curr = p
        
        p, q = head, prev
        
        while p and q:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        
        return True