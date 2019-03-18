class Solution:
    def replaceWords(self, roots: List[str], sentence: str) -> str:
        d = set(roots)
        
        res = sentence.split()
        
        for i in range(len(res)):
            word = res[i]
            
            for j in range(1, len(word)):
                if word[:j] in d:
                    res[i] = word[:j]
                    break
        
        res = ' '.join(res)
        
        return res