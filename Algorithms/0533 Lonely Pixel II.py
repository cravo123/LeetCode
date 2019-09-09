import collections

# Solution 1, almost brute-force
class Solution:
    def findBlackPixel(self, picture: List[List[str]], N: int) -> int:
        m, n = len(picture), len(picture[0]) if picture else 0
        
        cols = collections.defaultdict(list)
        rows = collections.defaultdict(list)
        
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    cols[j].append(i)
                    rows[i].append(j)
        
        d = {}
        
        for i, row in enumerate(picture):
            d[i] = ''.join(row)
        
        res = 0
        for j in range(n):
            if len(cols[j]) == N:
                if all(len(rows[i]) == N for i in cols[j]) and all(d[i] == d[cols[j][0]] for i in cols[j]):
                    res += N
        return res

# Solution 2, better implementation
