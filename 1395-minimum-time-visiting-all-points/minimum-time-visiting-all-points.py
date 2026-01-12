class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        cost = 0
        for ind in range(1, len(points)):
            dx = points[ind][0] - points[ind - 1][0]
            dy = points[ind][1] - points[ind - 1][1]

            numDiag = min(abs(dx), abs(dy))
            cost += abs(dx) + abs(dy) - numDiag
        
        return cost