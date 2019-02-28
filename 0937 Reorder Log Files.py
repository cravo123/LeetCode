class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = [word for word in logs if word.split()[1][0].isalpha()]
        digits_logs = [word for word in logs if not word.split()[1][0].isalpha()]
        
        letter_logs.sort(key=lambda word: [word.split()[1:], word.split()[0]])
        
        res = letter_logs + digits_logs
        
        return res

# We don't need to split the string actually, just use str.find(' ')