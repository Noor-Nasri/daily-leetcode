from heapq import heappop, heappush
class Solution:
    def dpSolve(self, eventInd, maxEvents):
        if (eventInd, maxEvents) in self.sols:
            return self.sols[(eventInd, maxEvents)]
        
        if eventInd >= len(self.nextEvents) or maxEvents == 0:
            return 0
        
        op1 = self.events[eventInd][2] + self.dpSolve(self.nextEvents[eventInd], maxEvents - 1)
        op2 = self.dpSolve(eventInd + 1, maxEvents)
        self.sols[(eventInd, maxEvents)] = max(op1, op2)
        return self.sols[(eventInd, maxEvents)]

    def buildNextEvents(self, events):
        nextEvents = [len(events) for i in range(len(events))]
        unsolved = []
        for ind in range(len(events)):
            st, en, v = events[ind]

            while unsolved and unsolved[0][0] < st:
                prevEd, prevInd = heappop(unsolved)
                nextEvents[prevInd] = ind
            
            heappush(unsolved, (en, ind))
        
        return nextEvents


    def maxValue(self, events: List[List[int]], k: int) -> int:
        self.events = sorted(events)
        self.nextEvents = self.buildNextEvents(self.events )
        self.sols = {}
        return self.dpSolve(0, k)
