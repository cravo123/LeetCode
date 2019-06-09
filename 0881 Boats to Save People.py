# Solution 1, greedy
# We need to prove that greedy is correct.
class Solution:
    def numRescueBoats(self, people: 'List[int]', limit: 'int') -> 'int':
        people.sort()
        
        i, j = 0, len(people) - 1
        res = 0
        while i <= j:
            v = people[i] + people[j]
            if v <= limit:
                i += 1
            j -= 1
            res += 1
        return res