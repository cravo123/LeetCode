# Solution 1, sliding-window
#   step 1, find out how many satisfied customers without using secret
#   step 2, sliding-window to find out how many customers can be turned to
#           satisfied by using the secret
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        res = sum(c * (1 - flag) for c, flag in zip(customers, grumpy))
        
        curr = curr_max = 0
        
        for i, c in enumerate(customers):
            if grumpy[i] == 1:
                curr += c
            if i >= X and grumpy[i - X] == 1:
                curr -= customers[i - X]
            
            curr_max = max(curr_max, curr)
        
        return res + curr_max