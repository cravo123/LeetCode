# First move curr to target as close as possible
# Then curr >= target, 
# if (curr - target) % 2 == 0, we only need to flip one number sign
# otherwise we need to move curr to be (curr - target) % 2 == 0
# This needs only 1 or 2 steps depending on whether i is odd or even
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        
        i = 0
        curr = 0
        
        while curr < target:
            curr += i
            i += 1
        i -= 1
        res = i
        
        if (curr - target) % 2 != 0:
            res += 1 if (i + 1) % 2 == 1 else 2
        
        return res