class Solution:
    def change(self, word):
        if word[0].lower() in 'aeiou':
            res = word
        else:
            res = word[1:] + word[0]
        return res + 'ma'
        
    def toGoatLatin(self, S: 'str') -> 'str':
        S = S.split()
        
        res = [self.change(word) + 'a' * (i + 1) for i, word in enumerate(S)]
        #res = [self.change(word) + 'a' * i for i, word in enumerate(S, 1)]
        return ' '.join(res)