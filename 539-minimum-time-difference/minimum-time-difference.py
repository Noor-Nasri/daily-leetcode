class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        values = [[int(e) for e in t.split(":")] for t in timePoints]
        numMinutes = sorted([v[0]*60 + v[1] for v in values])

        best = (24*60 - numMinutes[-1]) + numMinutes[0] # if looping around is best

        for ind in range(len(numMinutes) - 1):
            best = min(best, numMinutes[ind + 1] - numMinutes[ind])
        
        return best
        
        