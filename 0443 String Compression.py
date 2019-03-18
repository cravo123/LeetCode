class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        
        curr = chars[0]
        cnt = 0
        j = 0
        
        for c in chars:
            if curr == c:
                cnt += 1
            else:
                chars[j] = curr
                j += 1
                if cnt > 1:
                    width = len(str(cnt))
                    chars[j:(j + width)] = str(cnt)
                    j += width
                curr = c
                cnt = 1
        
        chars[j] = curr
        j += 1
        if cnt > 1:
            width = len(str(cnt))
            chars[j:(j + width)] = str(cnt)
            j += width
        
        return j