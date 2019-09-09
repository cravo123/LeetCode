from collections import Counter

# Solution 1, hash table
class Solution:
    def findLonelyPixel(self, picture: 'List[List[str]]') -> 'int':
        rows, cols = Counter(), Counter()
        
        m, n = len(picture), len(picture[0])
        
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    rows[i] += 1
                    cols[j] += 1
        
        res = 0
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B' and rows[i] == 1 and cols[j] == 1:
                    res += 1
        return res
        