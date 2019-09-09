# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1, simulation
# Use fast and slow pointers to find if there is a cycle or not.
# Then move fast pt back to head, and move both fast and slow one
# step a time, when they meet, that is where cycle begins.
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if fast is slow:
                break
        
        if fast is None or fast.next is None:
            return 
        
        fast = head
        
        while fast is not slow:
            fast = fast.next
            slow = slow.next
        
        return slow