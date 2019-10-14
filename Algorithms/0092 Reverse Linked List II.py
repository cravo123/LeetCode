# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1, simulation
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = curr = ListNode(0)
        dummy.next = head
        
        idx = 1
        
        while idx < m:
            curr = curr.next
            idx += 1
        
        # p_(m-1) -> p_m -> ...
        p_m_1 = curr
        p_m = curr.next
        
        pre = None
        while idx <= n + 1:
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp
            idx += 1
        
        p_n = curr
        
        p_m_1.next = pre
        p_m.next = p_n
        
        return dummy.next