import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        
        d = collections.Counter(tasks)
        v = d.most_common(1)[0][1]
        
        cnt = 0
        for c in d:
            if d[c] == v:
                cnt += 1
        # (v - 1) filling blocks each with width of n
        # we already filled (n - cnt + 1) for each block
        return len(tasks) + max(0, (n - cnt + 1) * (v - 1) - len(tasks) + cnt * v) 