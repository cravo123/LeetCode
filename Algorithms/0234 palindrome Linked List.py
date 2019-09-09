# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1,
# Split linked list to two equal parts, and iterate to check
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, curr = None, slow
        
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        p, q = head, prev
        
        while p and q:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        
        return True