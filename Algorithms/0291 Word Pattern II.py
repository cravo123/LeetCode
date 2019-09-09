# Solution 1, back-tracking 
# Similar idea to LC 290 Word Pattern
# The difference is that now we need to try each length from s
# Use d to maintain pattern[i] -> word in s
# Use seen to maintain used word
# By doing this, we have bijection property
class Solution:
    def dfs(self, i, j, pattern, s, d, seen):
        if i >= len(pattern) or j >= len(s):
            if i == len(pattern) and j == len(s):
                return True
            return False
        
        if pattern[i] in d:
            m = len(d[pattern[i]])
            if s[j:(j + m)] != d[pattern[i]]:
                return False
            return self.dfs(i + 1, j + m, pattern, s, d, seen)
        
        for length in range(1, len(s) - j + 1):
            word = s[j:(j + length)]
            if word in seen:
                continue
            seen.add(word)
            d[pattern[i]] = word
            if self.dfs(i + 1, j + length, pattern, s, d, seen):
                # If all we care is final result of True or False
                # We can omit the following back-tracking steps
                # If we need to generate all the "paths" along,
                # i.e. the function will not "return" here,
                # Then we do need back-tracking steps!
                seen.discard(word)
                del d[pattern[i]]
                return True
            seen.discard(word)
            del d[pattern[i]]
        return False
        
        
    def wordPatternMatch(self, pattern: str, S: str) -> bool:
        dc = {} # char -> word
        seen = set()
        
        return self.dfs(0, 0, pattern, S, dc, seen)