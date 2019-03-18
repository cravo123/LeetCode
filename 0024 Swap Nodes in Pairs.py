# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = curr = ListNode(0)
        curr.next = head
        
        while curr.next and curr.next.next:
            p, q = curr.next, curr.next.next
            tmp = curr.next.next.next
            
            curr.next = q
            q.next = p
            p.next = tmp
            
            curr = p
        
        return dummy.next

# Solution 3,
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        res = [0, 0]
        
        curr = 0
        for i, c in enumerate(nums):
            curr ^= (i + 1) ^ abs(c)
            if nums[abs(c) - 1] < 0:
                res[0] = abs(c)
            nums[abs(c) - 1] = - nums[abs(c) - 1]
        # curr = i ^ j, where i is the missing one and j is the one occurring twice
        
        res[1] = curr ^ res[0]
        
        return res