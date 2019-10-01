# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# For linked-list problems, there are tricks that are common to help you solve
# problems, and avoid corner cases
#   1. Add dummy head node,
#   2. Fast and Slow two pointers

# Solution 1, iteration
class Solution:
    def reverse(self, prev, end):
        # prev.next is start
        # reverse nodes from start to end(inclusive)
        start = prev.next
        p = end.next
        
        a, b = None, start
        while a is not end:
            c = b.next
            b.next = a
            a = b
            b = c
        
        prev.next = end
        start.next = p
        
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        
        curr = head
        cnt = 1
        
        while curr:
            if cnt == k:
                p = prev.next
                
                self.reverse(prev, curr)
                
                prev = p
                curr = p
                cnt = 0
            curr = curr.next
            cnt += 1
        
        return dummy.next

# Solution 2, Recursion is easier.
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        runner = head
        cnt = 0
        while runner and cnt < k:
            cnt += 1
            runner = runner.next
        
        if cnt == k:
            nxt_node = self.reverseKGroup(runner, k)
            
            # Then reverse First k node
            prev, curr = None, head
            while curr is not runner:
                tmp = curr.next
                curr.next = prev
                prev, curr = curr, tmp
            
            # append tail
            head.next = nxt_node
            head = prev
        
        return head                