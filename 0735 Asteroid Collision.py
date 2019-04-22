# Solution 1, using Stack
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