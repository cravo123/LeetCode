import bisect
# Solution 1, Counting
class Solution:
    def can_friend(self, a, b):
        # a friend b
        return 0.5 * a + 7 < b <= a
        
    def numFriendRequests(self, ages: List[int]) -> int:
        d = collections.Counter(ages)
        
        res = 0
        
        for a in d:
            for b in d:
                if self.can_friend(a, b):
                    res += d[a] * d[b]
                    if a == b:
                        res -= d[a]
        return res

# Solution 2, binary search
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        
        res = 0
        
        for i in range(len(ages)):
            a = bisect.bisect_right(ages, 0.5 * ages[i] + 7)
            b = bisect.bisect_right(ages, ages[i])
            
            res += max(b - a - 1, 0)
        
        return res

