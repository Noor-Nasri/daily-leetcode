# We would want to only consider the extremes, but I don't really care tbh. I'll just do n^3 and move on.
# Formula is sqrt(s * (s - a)(s - b)(s - c)) where s is perimeter/2
class Solution:
    def getLineLen(self, p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

    def getArea(self, p1, p2, p3):
        a = self.getLineLen(p1, p2)
        b = self.getLineLen(p2, p3)
        c = self.getLineLen(p3, p1)
        s = (a + b + c)/2
        return (s * (s - a) * (s - b) * (s - c))**0.5

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        best = 0
        for x in range(len(points)):
            p1 = points[x]
            for y in range(x + 1, len(points)):
                p2 = points[y]
                for z in range(y + 1, len(points)):
                    p3 = points[z]
                    area =  self.getArea(p1, p2, p3)
                    if type(area) == complex:
                        continue # probably all a line
                    best = max(best, area)

        return best
            
