class Solution:
    # For each two points, we compute the slope and add combinations as we go
    # The only issue is that we don't want to count cases where the same slope is using one of the two points
    # This is actually more general: We want the same slope, but not if all 4 points are on the same line.
    # So just store intercept point and uncount identical lines

    # Wrong answer: We double count rectangles, because they have two pairs.
    # How can we avoid this? If at point A we oberse slope B then perpendicular slope C..
    # idk how to solve this without n^3 to find all parallelograms 
    # oooh, I saw a hint: The MIDPOINT in lines B and C will match!
    # So now we count midpoints as long as those dont have the same slope


    def countTrapezoids(self, points: List[List[int]]) -> int:
        total = 0
        slopeCount = {}
        slopeAndInterceptCount = {}
        midpointCount = {}
        midpointAndSlopeCount = {}

        for ind1 in range(len(points)):
            x1, y1 = points[ind1]
            for ind2 in range(ind1 + 1, len(points)):
                x2, y2 = points[ind2]
                midpoint = ((x1 + x2)/2, (y1 + y2)/2)  

                if x1 == x2:
                    slope = "Vertical"
                    intercept = x1
                else:
                    exactSlope = (y2 - y1)/(x2 - x1)
                    slope = round(exactSlope, 7)
                    intercept = round(y1 - x1*exactSlope, 7)
                
                trapezoidCount = slopeCount.get(slope, 0)
                trapezoidExclusions = slopeAndInterceptCount.get((slope, intercept), 0)
                parallelogramCount = midpointCount.get(midpoint, 0)
                parallelogramExclusions = midpointAndSlopeCount.get((midpoint, slope), 0)
                
                slopeCount[slope] = trapezoidCount + 1
                slopeAndInterceptCount[(slope, intercept)] = trapezoidExclusions + 1
                midpointCount[midpoint] = parallelogramCount + 1
                midpointAndSlopeCount[(midpoint, slope)] = parallelogramExclusions + 1

                total += trapezoidCount - trapezoidExclusions - parallelogramCount + parallelogramExclusions
                
        return total
