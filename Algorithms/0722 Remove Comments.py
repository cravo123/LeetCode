# By Chong Chen, https://github.com/cravo123/LeetCode

# Solution 1, Finite-State-Machine
# Special chars are '//', '/*', '*/', but we need to check is_block state
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        curr = []
        is_block = False
        
        for line in source:
            i, n = 0, len(line)
            while i < n:
                if line[i:(i + 2)] == '/*' and not is_block:
                    is_block = True
                    i += 2
                elif line[i:(i + 2)] == '*/' and is_block:
                    is_block = False
                    i += 2
                elif is_block:
                    i += 1
                    continue
                elif line[i:(i + 2)] == '//':
                    break
                else:
                    curr.append(line[i])
                    i += 1
            
            if curr and not is_block:
                res.append(''.join(curr))
                curr = []
        
        return res