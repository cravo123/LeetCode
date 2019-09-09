import datetime

# Solution 1, simulation
class Solution:
    def dayOfYear(self, date: str) -> int:
        big = set([1, 3, 5, 7, 8, 10, 12]) # monthes with 31 days
        y, m, d = date.split('-')
        y, m, d = map(int, [y, m, d])
        
        res = d
        i = 1
        while i < m:
            if i in big:
                res += 31
            elif i == 2:
                if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
                    res += 29
                else:
                    res += 28
            else:
                res += 30
            i += 1
        
        return res

# Solution 2, built-in
# From engineering perspective, this should be the preferred way.
class Solution:
    def dayOfYear(self, date: str) -> int:
        y, m, d = map(int, date.split('-'))
        
        res = (datetime.date(y, m, d) - datetime.date(y, 1, 1)).days + 1
    
        return res