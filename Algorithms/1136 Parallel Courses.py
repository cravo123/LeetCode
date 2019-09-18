import collections

# Solution 1, topological-sorting
class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        nxt = collections.defaultdict(set) # prerequisite -> next_course
        cnt = collections.Counter()
        
        for x, y in relations:
            nxt[x].add(y)
            cnt[y] += 1
        
        curr = [i for i in range(1, N + 1) if cnt[i] == 0]
        seen = len(curr)
        steps = 0
        
        while curr:
            steps += 1
            tmp = set()
            for x in curr:
                for y in nxt[x]:
                    cnt[y] -= 1
                    if cnt[y] == 0:
                        tmp.add(y)
                        seen += 1
            curr = tmp
        
        return steps if seen == N else -1