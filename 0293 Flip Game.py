class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        s = list(s)
        
        res = []
        
        for i in range(len(s) - 1):
            if s[i:(i + 2)] == ['+', '+']:
                t = s[::]
                t[i:(i + 2)] = ['-', '-']
                res.append(''.join(t))
        return res