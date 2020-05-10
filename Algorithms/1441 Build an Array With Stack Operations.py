# Solution 1, simulation
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        
        need = 1
        
        for c in target:
            if c == need:
                res.append('Push')
                need += 1
            elif c > need:
                res.extend(['Push', 'Pop'] * (c - need))
                res.append('Push')
                need = c + 1
        
        return res