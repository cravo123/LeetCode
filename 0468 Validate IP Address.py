import string

class Solution:
    def check_ipv4(self, IP):
        IP = IP.split('.')
        
        if len(IP) != 4:
            return False
        
        for x in IP:
            if not x.isdigit():
                return False
            v = int(x)
            if v > 255 or len(x) > 1 and x[0] == '0':
                return False
        return True

    def check_ipv6(self, IP):
        IP = IP.split(':')
        
        if len(IP) != 8:
            return False
        
        for x in IP:
            if any(c not in string.hexdigits for c in x):
                return False
            if len(x) > 4 or len(x) == 0:
                return False
        return True
        
        
    def validIPAddress(self, IP: str) -> str:
        if '.' in IP and self.check_ipv4(IP):
            res = 'IPv4'
        elif ':' in IP and self.check_ipv6(IP):
            res = 'IPv6'
        else:
            res = 'Neither'
        
        return res