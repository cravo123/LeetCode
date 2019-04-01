import collections

# Solution 1, loop through sorted A
class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        d = collections.Counter(A)
        
        A.sort(key=lambda x: [abs(x), x])
        
        for c in A:
            if d[c] == 0:
                continue
            if c == 0:
                if d[c] % 2 == 1:
                    return False
                d[c] = 0
            else:
                d[2 * c] -= d[c]
                if d[2 * c] < 0:
                    return False
                d[c] = 0
        return True

# Solution 2, loop through sorted d's keys
class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        d = collections.Counter(A)
        
        for c in sorted(A, key=abs):
            if d[c] == 0:
                continue
            if c == 0:
                if d[c] % 2 == 1:
                    return False
                d[c] = 0
            else:
                d[2 * c] -= d[c]
                if d[2 * c] < 0:
                    return False
                d[c] = 0
        return True