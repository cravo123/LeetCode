import collections

# Say there are n rabbits having same color, then there should be at
# most n rabbits saying there are (n - 1) rabbits having same color as
# itself.
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d = collections.Counter(answers)
        
        res = 0
        
        for v, cnt in d.items():
            res += ((cnt - 1) // (v + 1) + 1) * (v + 1)
        
        return res