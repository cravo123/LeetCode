# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1, fast and slow pointer
# This trick is one of the few algorithms in linked list problems
class Solution:
    def middleNode(self, head: 'ListNode') -> 'ListNode':
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# Solution 2, first get length, then traverse to half
class Solution:
    def length(self, head):
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        return n
        
    def middleNode(self, head: 'ListNode') -> 'ListNode':
        n = self.length(head)
        
        n = n // 2
        i = 0
        curr = head
        
        while i < n:
            i += 1
            curr = curr.next
        return curr