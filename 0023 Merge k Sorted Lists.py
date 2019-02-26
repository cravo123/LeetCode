# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from heapq import *

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = []
        
        idx = 0
        for p in lists:
            if p:
                heappush(q, (p.val, idx, p))
                idx += 1
        
        dummy = curr = ListNode(0)
        
        while q:
            p = heappop(q)
            curr.next = p[2]
            curr = curr.next
            
            if p[2].next:
                heappush(q, (p[2].next.val, idx, p[2].next))
                idx += 1
        
        curr.next = None
        
        return dummy.next