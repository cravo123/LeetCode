import collections

class Solution:
    def parse(self, info, d):
        info = info.split()
        
        curr_dir = info[0]
        
        for name in info[1:]:
            idx = name.index('(')
            content = name[(idx + 1):-1]
            d[content].append('/'.join([curr_dir, name[:idx]]))
        
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        
        for path in paths:
            self.parse(path, d)
        
        res = [content for content in d.values() if len(content) > 1]
        
        return res