class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        d = {c:i for i, c in enumerate(S)}
        res = []
        curr = float('-inf')
        cnt = 0
        for i, c in enumerate(S):
            curr = max(curr, d[c])
            cnt += 1
            if curr == i:
                res.append(cnt)
                cnt = 0
        return res