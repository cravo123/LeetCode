import collections

# Solution 1, simulation
# simulate index,
# idx points to the sorted deck value we want to fill in final result
# q stores index candidates, and simulate revealing card process
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        q = collections.deque(range(n))
        
        res = [0 for _ in deck]
        idx = 0
        while q:
            i = q.popleft()
            res[i] = deck[idx]
            idx += 1
            if q:
                q.append(q.popleft())
        return res