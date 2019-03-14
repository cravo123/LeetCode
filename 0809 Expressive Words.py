class Solution:
    def calc(self, word):
        res = []
        if not word:
            return res
        curr = word[0]
        curr_cnt = 0
        
        for c in word:
            if c == curr:
                curr_cnt += 1
            else:
                res.append([curr, curr_cnt])
                curr = c
                curr_cnt = 1
        res.append([curr, curr_cnt])
        
        return res
    
    def is_eligible(self, target, curr):
        if len(target) != len(curr):
            return False
        
        for a, b in zip(target, curr):
            if a == b:
                continue
            if a[0] != b[0] or a[1] < b[1] or (b[1] < a[1] < 3):
                return False
        return True
    
    def expressiveWords(self, S: str, words: List[str]) -> int:
        
        target = self.calc(S)
        res = 0
        for word in words:
            curr = self.calc(word)
            if self.is_eligible(target, curr):
                res += 1
        
        return res