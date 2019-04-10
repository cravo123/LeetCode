class Solution:
    def change(self, num):
        res = bin(num)[2:]
        if len(res) > 8:
            return res[-8:]
        res = '0' * (8 - len(res)) + res
        
        return res
    
    def count(self, v):
        res = 0
        i = 0
        while i < len(v) and v[i] == '1':
            res += 1
            i += 1
        
        return res
    
    def validUtf8(self, data: List[int]) -> bool:
        n = len(data)
        i = 0
        
        while i < n:
            v = self.change(data[i])
                        
            if v[0] == '0':
                i += 1
            else:
                cnt = self.count(v)
                if not (2 <= cnt <= 4):
                    return False
                if n < i + cnt or any(self.change(data[j])[:2] != '10' for j in range(i + 1, i + cnt)):
                    return False
                i += cnt
        return True