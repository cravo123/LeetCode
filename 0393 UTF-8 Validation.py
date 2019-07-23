# Solution 1, simulation
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i, n = 0, len(data)
        
        while i < n:
            v = format(data[i], '#010b')[2:][-8:]
            idx = v.find('0')
            if idx == 0:
                i += 1
            elif idx in [2, 3, 4]:
                if i + idx > n or any(format(data[k], '#010b')[2:][:2] != '10' for k in range(i + 1, i + idx)):
                    return False
                i += idx
            else:
                return False
        return True