class Solution:
    # I think the optimal approach here is to do a sweep while tracking smallest L still running
    # Then any other intervals that end can be excluded, ie the first interval must end first.
    # But for these constraints, I can just do n^2 so I'll do that quickly 

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        total = 0
        for ind1 in range(len(intervals)):
            a, b = intervals[ind1]
            covered = False

            for ind2 in range(len(intervals)) :
                if ind1 == ind2:
                    continue

                c, d = intervals[ind2]
                if c <= a and b <= d:
                    covered = True
                    break
            
            if not covered:
                total += 1
        
        return total