class Solution:
    def customSortString(self, S: str, T: str) -> str:
        d = {c:i for i, c in enumerate(S)}
        
        T = list(T)
        T.sort(key=lambda x: d[x] if x in d else -1)
        res = ''.join(T)

        return res
