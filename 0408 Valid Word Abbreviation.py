class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        m, n = map(len, (word, abbr))
        
        i = j = 0
        
        while i < m and j < n:
            if abbr[j].isalpha():
                if abbr[j] != word[i]:
                    return False
                i += 1
                j += 1
            else:
                curr = 0
                k = j
                while j < n and abbr[j].isdigit():
                    curr = curr * 10 + int(abbr[j])
                    j += 1
                if curr == 0 or(curr > 0 and abbr[k] == '0'):
                    return False
                i += curr
        return i == m and j == n