class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = [word for word in logs if word.split()[1][0].isalpha()]
        digits_logs = [word for word in logs if not word.split()[1][0].isalpha()]
        
        letter_logs.sort(key=lambda word: [word.split()[1:], word.split()[0]])
        
        res = letter_logs + digits_logs
        
        return res

# Solution 1.1,
# We don't need to split the string actually, just use str.find(' ')
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        
        for s in logs:
            idx = s.find(' ')
            
            if s[idx + 1].isalpha():
                letter_logs.append([s[idx:], s[:idx]])
            else:
                digit_logs.append(s)
        
        letter_logs.sort()
        
        res = [first + second for second, first in letter_logs] + digit_logs
        
        return res