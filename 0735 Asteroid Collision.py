# Solution 1, Stack
# Easy to understand
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        q = []
        
        for c in asteroids:
            if c > 0:
                q.append(c)
            else:
                flag = True
                while q and q[-1] > 0:
                    if q[-1] == abs(c):
                        q.pop()
                        flag = False
                        break
                    elif q[-1] < abs(c):
                        q.pop()
                    else:
                        flag = False
                        break
                if flag:
                    q.append(c)
        return q

# Solution 1.1, stack, more elegant solution using while ... else...
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        q = []
        
        for c in asteroids:
            if c > 0:
                q.append(c)
            else:
                while q and q[-1] > 0:
                    if q[-1] < abs(c):
                        q.pop()
                    elif q[-1] > abs(c):
                        break
                    else:
                        q.pop()
                        break
                else:
                    q.append(c)
        return q