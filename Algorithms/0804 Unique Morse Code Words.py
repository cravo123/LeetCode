# Solution 1, hash set
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d = [".-","-...","-.-.","-..",".",
             "..-.","--.","....","..",".---",
             "-.-",".-..","--","-.","---",".--.",
             "--.-",".-.","...","-","..-","...-",
             ".--","-..-","-.--","--.."]
        
        res = set()
        
        for word in words:
            res.add(''.join(d[ord(c) - ord('a')] for c in word))
        
        return len(res)