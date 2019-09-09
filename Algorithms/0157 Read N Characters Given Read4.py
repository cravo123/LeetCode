"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
# Solution 1, assume buf is large enough to hold all returned chars
class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        tmp = ['' for _ in range(4)]
        
        cnt = 0
        while cnt < n:
            curr = read4(tmp)            
            buf[cnt:(cnt + curr)] = tmp
            cnt += curr
            if curr < 4:
                break
        
        return min(cnt, n)

# Solution 2, more precise control of buf
class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        tmp = ['' for _ in range(4)]
        
        cnt = 0
        while cnt < n:
            curr = read4(tmp)
            curr = min(curr, n - cnt)
            buf[cnt:(cnt + curr)] = tmp[:curr]
            cnt += curr
            
            if curr < 4:
                break
        
        return min(cnt, n)