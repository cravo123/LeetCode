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