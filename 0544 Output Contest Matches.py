class Solution:
    def findContestMatch(self, n: int) -> str:
        q = [str(i) for i in range(1, n + 1)]
        
        while len(q) > 1:
            tmp = []
            i, j = 0, len(q) - 1
            while i < j:
                tmp.append(('(%s,%s)') % (q[i], q[j]))
                i += 1
                j -= 1
            q = tmp
        return q[0]