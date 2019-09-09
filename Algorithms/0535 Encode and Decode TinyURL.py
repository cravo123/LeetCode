import itertools
import string

# Solution 1, use increasing index
class Codec:
    short_2_long = {}
    long_2_short = {}
    idx = 0
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.long_2_short:
            self.idx += 1
            self.long_2_short[longUrl] = self.idx
            self.short_2_long[self.idx] = longUrl
        
        return self.long_2_short[longUrl]
        
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.short_2_long[shortUrl]

class Codec:
    candidates = string.ascii_letters + string.digits
    long_2_short = {}
    short_2_long = {}
    size = 6

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.long_2_short:
            while True:
                tmp_str = itertools.permutations(self.candidates, self.size)
                if tmp_str not in self.short_2_long:
                    self.short_2_long[tmp_str] = longUrl
                    self.long_2_short[longUrl] = tmp_str
                    break
        return self.long_2_short[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.short_2_long[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))