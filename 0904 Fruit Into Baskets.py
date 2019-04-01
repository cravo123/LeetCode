import collections

# Solution 2, longest subarray with at most 2 distinct elements
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        res = 0
        n = len(tree)
        d = collections.Counter()
        i, j = 0, -1
        
        while i < n:
            d[tree[i]] += 1
            
            while len(d) > 2:
                j += 1
                d[tree[j]] -= 1
                if not d[tree[j]]:
                    del d[tree[j]]
            res = max(res, i - j)
            i += 1
        return res