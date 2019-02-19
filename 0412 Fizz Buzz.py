class Solution:
    def change(self, i):
        if i % 15 == 0:
            res = 'FizzBuzz'
        elif i % 5 == 0:
            res = 'Buzz'
        elif i % 3 == 0:
            res = 'Fizz'
        else:
            res = str(i)
        return res
    
    def fizzBuzz(self, n: 'int') -> 'List[str]':
        res = [self.change(i) for i in range(1, n + 1)]
        
        return res

# More general solution when it is FizzBuzzJazz
class Solution:
    def change(self, i):
        res = ''
        d = {3: 'Fizz', 5: 'Buzz'}
        for v in [3, 5]:
            if i % v == 0:
                res += d[v]
        
        return res if res else str(i)
        
        
    def fizzBuzz(self, n: 'int') -> 'List[str]':
        res = [self.change(i) for i in range(1, n + 1)]
        
        return res