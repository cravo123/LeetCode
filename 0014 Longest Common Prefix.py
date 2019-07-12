# Solution 1, simulation
# try each possible length from largest to smallest
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        n = len(strs[0])
        for c in strs:
            n = min(n, len(c))
        
        for i in range(n):
            if any(strs[j][i] != strs[0][i] for j in range(len(strs))):
                return strs[0][:i]
        return strs[0][:n]

# Solution 1.1, simulation
# Use first element to as candidate to try
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        q = strs[0]
        
        for i in range(1, len(strs)):
            k = 0
            for a, b in zip(q, strs[i]):
                if a == b:
                    k += 1
                else:
                    break
            q = q[:k]
        
        return q

# Solution 2, vertical iteration
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        n = len(strs)
        
        k = min(len(s) for s in strs)
        
        for i in range(k):
            if any(s[i] != strs[0][i] for s in strs):
                return strs[0][:i]
        
        return strs[0][:k]