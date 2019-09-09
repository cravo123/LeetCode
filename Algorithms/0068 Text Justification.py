# Solution 1, it is good to do one thing at a time. This will reduce
# complexity a lot. For this specific problem, we can seprate it as
# two steps.
#   1. Determine words for each line,
#   2. Then justify all lines except last one.
class Solution:
    def justify(self, path, maxWidth):
        n = len(path)
        spaces = maxWidth - sum(len(word) for word in path)
        if n == 1:
            return path[0] + ' ' * spaces
        
        res = []
        
        for i, word in enumerate(path):
            res.append(word)
            if i == n - 1:
                continue
            t = (spaces - 1) // (n - i - 1) + 1
            spaces -= t
            res.append(' ' * t)
        
        res = ''.join(x for x in res)
        
        return res
        
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        q = []
        path = []
        
        curr = 0
        
        for word in words:
            if curr + len(word) <= maxWidth:
                curr += len(word) + 1
                path.append(word)
            else:
                q.append(path)
                path = [word]
                curr = len(word) + 1
        q.append(path)
        
        res = [self.justify(path, maxWidth) for path in q[:-1]]
        last_line = ' '.join(x for x in q[-1])
        res.append(last_line + ' ' * (maxWidth - len(last_line)))
        
        return res