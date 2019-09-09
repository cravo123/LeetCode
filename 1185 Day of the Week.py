import datetime

# Solution 1, simulation using built-in 
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        d = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        
        idx = datetime.date(year, month, day).weekday()
        
        return d[idx]