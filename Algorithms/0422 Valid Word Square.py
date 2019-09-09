class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        if not words:
            return True
        m, n = len(words), max(len(row) for row in words)
        
        if m != n:
            return False
        
        for i in range(n):
            for j in range(i):
                a = words[i][j] if j < len(words[i]) else ''
                b = words[j][i] if i < len(words[j]) else ''
                if a != b:
                    return False
        return True