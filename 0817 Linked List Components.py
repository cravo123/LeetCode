# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1, simulation using hashmap
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        d = set(G)
        res = 0
        
        pre = None
        curr = head
        
        while curr:
            if pre not in d and curr.val in d:
                res += 1
            pre = curr.val
            curr = curr.next
        return res