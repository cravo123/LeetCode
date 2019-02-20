class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        idx = [".-","-...","-.-.","-..",".","..-.",
                "--.","....","..",".---","-.-",".-..",
                "--","-.","---",".--.","--.-",".-.",
                "...","-","..-","...-",".--","-..-","-.--","--.."]
        
        res = set()
        
        for word in words:
            tmp = ''.join(idx[ord(c) - ord('a')] for c in word)
            res.add(tmp)
        
        return len(res)