import collections

# It is always easier and clearer to separate functionalities to smaller functions
class Solution:
    def case_insensitive(self, wordlist):
        d = collections.defaultdict(list) # Actually only need to cache the first occurrence
        for word in wordlist:
            d[word.lower()].append(word)
        
        return d
    
    def normalize_word(self, word):
        res = ['*' if c.lower() in 'aeiou' else c.lower() for c in word]
        res = ''.join(res)
        
        return res
    
    def vowel_error(self, wordlist):
        d = collections.defaultdict(list)
        for word in wordlist:
            tmp = self.normalize_word(word)
            d[tmp].append(word)
        
        return d

    def check(self, word, exact_match, case_insensitive_d, vowel_error_d):
        if word in exact_match:
            return word
        if word.lower() in case_insensitive_d:
            return case_insensitive_d[word.lower()][0]
        tmp = self.normalize_word(word)
        if tmp in vowel_error_d:
            return vowel_error_d[tmp][0]
        
        return ''
    
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exact_match = set(wordlist)
        
        case_insensitive_d = self.case_insensitive(wordlist)
        
        vowel_error_d = self.vowel_error(wordlist)
        
        res = [self.check(word, exact_match, case_insensitive_d, vowel_error_d) for word in queries]
        
        return res
        