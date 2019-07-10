import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1, priority queue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = [[p.val, i, p] for i, p in enumerate(lists) if p] # in case p.val is equal, we use i
        heapq.heapify(q)
        
        dummy = curr = ListNode(None)
        
        while q:
            _, idx, p = heapq.heappop(q)
            curr.next = p
            curr = p
            
            if p.next:
                heapq.heappush(q, [p.next.val, idx, p.next])
        
        return dummy.next