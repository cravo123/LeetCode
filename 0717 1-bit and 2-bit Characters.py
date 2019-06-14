# Solution 1, simulation
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        
        i = 0
        
        while i < n:
            j = i
            if bits[i] == 0:
                i += 1
            else:
                i += 2
        return i == j + 1

# Solution 1.1, a more elegant implementation
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        
        i = 0
        
        while i < n - 1: # gotcha
            if bits[i] == 0:
                i += 1
            else:
                i += 2
        
        return i == n - 1