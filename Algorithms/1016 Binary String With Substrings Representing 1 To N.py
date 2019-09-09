# Solution 1, Brute-Force
# We start from N so it can be early-terminated
class Solution:
    def queryString(self, S: str, N: int) -> bool:
        while N >= 1:
            x = bin(N)[2:]
            if x not in S:
                return False
            N -= 1
        return True

# Solution 2, check each value built from S
# O(m * min(m, log N))
class Solution:
    def queryString(self, S: str, N: int) -> bool:
        d = set()
        m = len(S)
        
        for i in range(m):
            if S[i] == '0':
                continue
            curr = 0
            j = i
            while j < m and curr < N:
                curr = (curr << 1) + int(S[j]) # gotcha, bit operation precedence
                j += 1
                if 0 < curr <= N:
                    d.add(curr)
                
        return len(d) == N