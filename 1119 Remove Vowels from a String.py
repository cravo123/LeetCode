# Solution 1, simulation
class Solution:
    def removeVowels(self, S: str) -> str:
        res = [c for c in S if c not in 'aeiou']
        
        return ''.join(res)