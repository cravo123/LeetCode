# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1, simulation
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        
        curr = head
        while curr:
            res = res * 2 + curr.val
            curr = curr.next
        
        return res