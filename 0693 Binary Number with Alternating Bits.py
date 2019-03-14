class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        pre = -1
        while n > 0:
            n, v = divmod(n, 2)
            if v == pre:
                return False
            pre = v
        return True