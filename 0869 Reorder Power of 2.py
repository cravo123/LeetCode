import collections
import itertools

# Solution 1, brute-force, enumerate all possibilities
# We are comparing sorted string representation of a number.
# Actually we can directly use Counter to compare numbers
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        i = 1
        target = ''.join(list(sorted(str(N))))
        
        while len(str(i)) <= len(target):
            v = ''.join(list(sorted(str(i))))
            
            if v == target:
                return True
            i *= 2
        
        return False

# Solution 2, brute-force, use Counter to check string identity
# Should remember that if order doesn't matter, then we can use both sorted
# string and Counter to check if two strings are the "same"
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        target = collections.Counter(str(N))
        
        i = 1
        while len(str(i)) <= len(str(N)):
            curr = collections.Counter(str(i))
            
            if curr == target:
                return True
            
            i *= 2
        
        return False

# Solution 3, a different idea
# check permutation of str(N) to see if it is power of 2
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        for c in itertools.permutations(str(N)):
            if c[0] != '0':
                v = int(''.join(c))
                
                while v > 1 and v % 2 == 0:
                    v //= 2
                
                if v == 1:
                    return True
        return False

# Solution 4, manual implement permutations
class Solution:
    def dfs(self, s, seen, path, res):
        if len(path) == len(s):
            res.append(''.join(path))
            return
        
        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1] and seen[i - 1] is False:
                continue
            if seen[i] == False:
                seen[i] = True
                path.append(s[i])
                self.dfs(s, seen, path, res)
                path.pop()
                seen[i] = False
        
    def permutations(self, s):
        res = []
        path = []
        s = ''.join(list(sorted(s)))
        
        seen = [False for _ in s]
        
        self.dfs(s, seen, path, res)
        
        res = [int(x) for x in res if x[0] != '0']
        
        return res
        
    def reorderedPowerOf2(self, N: int) -> bool:
        for v in self.permutations(str(N)):
            while v > 1 and v % 2 == 0:
                v //= 2
            
            if v == 1:
                return True
        
        return False