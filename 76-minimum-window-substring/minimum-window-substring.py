from collections import deque

class Solution:
    def get_ind(self, c: str) -> int:
        ind = ord(c)
        if ind >= 97 : ind -= 97
        else: ind -= (65 - 26)
        return ind

    def minWindow(self, s: str, t: str) -> str:
        # First, count occur needed
        # Then loop through .. if letter is needed, count it
        # If full match, store it as best if best
        # Once we include too many, we can exclude the earliest
        # At every point, we store EARLIEST, and LATEST. 
        word_counts = [0 for i in range(26*2)]
        for char in t:
            word_counts[self.get_ind(char)] += 1
        
        missing = {}
        for ind, val in enumerate(word_counts):
            if val > 0: missing[ind] = val


        included = deque()
        self.best = None

        def filterExtras():
            while True:
                top_ind = self.get_ind(s[included[0]])
                if word_counts[top_ind] < 0:
                    # Can shift left side of window up
                    included.popleft()
                    word_counts[top_ind] += 1

                    # Check if this is best so far
                    cur = (included[0], included[-1] + 1)
                    if (self.best == None) or (cur[1] - cur[0]) < (self.best[1] - self.best[0]):
                        self.best = cur
                else:
                    break
        
        # Every time we include one, we put [char, ind]
        # Once the top char is not needed, we pop as many as we can
        for i in range(len(s)):
            count_ind = self.get_ind(s[i])

            if missing:
                # We still have not found first solution, see if this helps
                word_counts[count_ind] -= 1
                included.append(i)
                if not count_ind in missing: 
                    continue
                missing[count_ind] -= 1

                if not missing[count_ind]: # now 0
                    del missing[count_ind]
                    if not missing: # No more missing, found first solution
                        self.best = (included[0], i+1)
                        filterExtras()

            else:
                # We are trying to optimize this window. 
                # Include it, and if we can start popping the front then do it
                word_counts[count_ind] -= 1
                included.append(i)
                filterExtras()
                        
        if self.best == None:
            return ""

        filterExtras()
        return s[self.best[0]:self.best[1]]
        