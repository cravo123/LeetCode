import random
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1, reseroir sampling
# Idea is that, given we are at index n, 
# there is (n - 1) / n probability that we retain values at hand
# and there is 1 / n probability that we update to new value
# Given conditional probability, we know that each value has equal
# probability to be chosen.
# Similar idea can be choosing k elements from n population
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        curr = self.head
        res = curr.val
        idx = 2
        
        while curr.next:
            v = random.randint(1, idx)
            if v == idx:
                res = curr.next.val
            idx += 1
            curr = curr.next
        
        return res

# Solution 2, cache all values first
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.q = []
        curr = head
        
        while curr:
            self.q.append(curr.val)
            curr = curr.next
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return random.choice(self.q)



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()