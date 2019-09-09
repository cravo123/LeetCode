import bisect
import collections

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.t = []
        self.idx = []
        
        d = collections.Counter()
        curr_max = 0
        max_idx = None
        for time, person in zip(times, persons):
            d[person] += 1
            if curr_max <= d[person]:
                curr_max = d[person]
                max_idx = person
                self.idx.append(person)
            else:
                self.idx.append(max_idx)
            self.t.append(time)

    def q(self, t: int) -> int:
        person = bisect.bisect_right(self.t, t)
        
        return self.idx[person - 1]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)