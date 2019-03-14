import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        
        for word in strs:
            d[''.join(sorted(word))].append(word)
        
        res = list(d.values())
        
        return res