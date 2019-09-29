# Solution 1, stack simulation
# Use a stack to store (char, count) pair
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        q = [['', 0]]
        
        for c in s:
            if c == q[-1][0]:
                q[-1][1] += 1
                if q[-1][1] == k:
                    q.pop()
            else:
                q.append([c, 1])
        
        res = ''.join(c * cnt for c, cnt in q)
        
        return res