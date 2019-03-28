# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

# Candidate will be the candidate celebrity.
# As long as there is a real celebrity, candidate
# will always be the right one. This is because once
# candidate be celebrity index, it will never leave, similar
# to absorbing status in Markov Chain.
class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        # two-pass
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        
        for i in range(n):
            if candidate == i:
                continue
            # Note, now candidate is the celebrity candidate
            # we want to make sure that if candidate knows anyone
            # or someone doesn't know candidate, then candidate is
            # not celebrity
            if knows(candidate, i) or not knows(i, candidate):
                return -1
        
        return candidate