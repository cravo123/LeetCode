class Solution:
    def generate(self, left, right):
        if left == right:
            res = str(left)
        else:
            res = '%d->%d' % (left, right)
        return res
        
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        q = []
        prev = lower
        
        for c in nums + [upper + 1]:
            if prev < c:
                q.append(self.generate(prev, c - 1))
            prev = c + 1
        return q

# Solution 2, another idea
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        q = []
        
        prev = lower
        
        for c in nums + [upper + 1]:
            if c < prev:
                continue
            
            if prev + 1 == c:
                q.append(str(prev))
            elif prev + 1 < c:
                q.append('%d->%d' % (prev, c - 1))
            prev = c + 1
        
        return q