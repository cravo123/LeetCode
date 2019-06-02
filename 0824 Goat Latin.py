# Solution 1, simulation
class Solution:
    def change(self, word, idx):
        if word[0].lower() in 'aeiou':
            res = word
        else:
            res = word[1:] + word[0]
        
        res = res + 'ma' + 'a' * idx
        
        return res
        
    def toGoatLatin(self, S: str) -> str:
        
        words = S.split()
        
        res = ' '.join(self.change(word, i + 1) for i, word in enumerate(words))
        
        return res