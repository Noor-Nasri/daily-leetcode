class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2: return len(points)

        bestNum = 2
        points = sorted(points, key = lambda x: x[0])

        for i1 in range(len(points)):
            p1 = points[i1]
            lines = {}
            for i2 in range(i1 + 1, len(points)):
                p2 = points[i2]

                if (p1[0] == p2[0]):
                    m = 'inf'
                else:
                    m = (p2[1] - p1[1])/(p2[0] - p1[0])
                
                if m in lines:
                    lines[m] += 1

                    if lines[m] > bestNum:
                        bestNum = lines[m]
                else:
                    lines[m] = 2

        return bestNum