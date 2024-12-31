class Solution:
    def solveDP(self, dayInd, dayCutoff):
        if (dayInd, dayCutoff) in self.sols:
            return self.sols[(dayInd, dayCutoff)]
        
        if dayInd == len(self.days):
            return 0
        
        if self.days[dayInd] < dayCutoff:
            sol = self.solveDP(dayInd + 1, dayCutoff)
        else:
            sol = min(
                self.costs[0] + self.solveDP(dayInd + 1, self.days[dayInd] + 1),
                self.costs[1] + self.solveDP(dayInd + 1, self.days[dayInd] + 7),
                self.costs[2] + self.solveDP(dayInd + 1, self.days[dayInd] + 30),
            )

        
        self.sols[(dayInd, dayCutoff)] = sol
        return sol


    def mincostTickets(self, days: List[int], costs: List[int]) -> int:  
        self.sols = {}
        self.days = days
        self.costs = costs
        return self.solveDP(0, 0)

