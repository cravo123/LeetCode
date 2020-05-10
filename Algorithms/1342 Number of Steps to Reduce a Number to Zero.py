# Solution 1, simulation
class Solution:
    def numberOfSteps (self, num: int) -> int:
        steps = 0
        
        while num > 0:
            steps += 1
            if num % 2 == 1:
                num -= 1
            else:
                num //= 2
        
        return steps