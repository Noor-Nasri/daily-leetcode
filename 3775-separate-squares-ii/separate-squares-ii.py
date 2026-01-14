class Solution:
    # The solution to the medium variation would work fine here, except we need non-overlapping rects
    # Removing overlaps is not trivial because there can be n^2 overlaps, and we cant afford n^2.
    # Even if we use a tree to seperate rects, then left/right/up/down overlaps create new branches.
    # It might potentially work but the time complexity is hard to understand

    # Alternate idea: Iterate on all CORNER y values, and compute the total space between the 2 y values
    # Because those are corners, all rects found within them fully extend on the y. So we only need to merge across x-axis
    # BUT: we cannot recompute this overlap between every pair - because there can be n squares being merged
    # IDEA: sliding window-ish. Once we include a square, it stays accounted for  until popped.
    # SOLUTION: Iterate on 10^5 y values while adding/popping each square once into the 10^5 x value range
    # Jeez, this idea took me 60 minutes of brainstorming. This is indeed hard.
    
    # PROBLEM 2: Even after splitting into just x values, we need a way to merge them without looping through all active squares
    # SOLUTION: Since its now 1d, we can do a tree. Each node has left, right, within, and a variable for leftoverlapend and rightoverlapstart
    # So to add a node: Its log(n) as you just go into the branch. If you completely cover a node, you just take its place and it goes within.
    # To remove a node: Also log(n). You replace it by [within] or [successor]

    # I am 99% this is solvable but I dont want to implement a custom tree struct for this.
    # After 2 hours of thinking, I will indeed go with a public solution :(

    """
    
    def computeInds(self, squares):
        xValues = set()
        yValues = set()
        for x, y, length in squares: 
            xValues.add(x)
            xValues.add(x + length)
            yValues.add(x)
            yValues.add(x + length)
        
        yValues = sorted(list(yValues))
        xValues = sorted(list(xValues))
        xValueToInd = {xValues[i] : i for i in range(len(xValues))}
        spaceAfterXInd = []
        for i in range(len(xValues) - 1):
            spaceAfterXInd.append(xValues[i + 1] - xValues[i])
        
        return yValues, xValueToInd, spaceAfterXInd


    def convertSquaresIntoRanges(self, squares):
        yValueToOpenedXRanges = {}
        yValueToClosedXRanges = {}
        for x, y, length in squares: 
            if y not in yValueToOpenedXRanges:
                yValueToOpenedXRanges[y] = []
            
            if y + length not in yValueToClosedXRanges:
                yValueToClosedXRanges[y + length] = []

            yValueToOpenedXRanges[y].append((x, x + length))
            yValueToClosedXRanges[y + lengt].append((x, x + length))

        return yValueToOpenedXRanges, yValueToClosedXRanges

    def computeSpaceBelowEveryY(self, yValues, yValueToOpenedXRanges, yValueToClosedXRanges, xValueToInd, spaceAfterXInd):
        spaceBelow = [0]
        xSpaceFillCounts = [0 for i in range(len(spaceAfterXInd))]
        xSpaceFilled = 0
        totalSpaceAccountedFor = 0

        for yInd in range(1, len(yValues)):
            # Include/Exclude all rects based on yInd - 1
            # Then count the region between the two inds as filled space, and update the spaceBelow for yInd

            pass

        return spaceBelow
    """


    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))

        events.sort()
        xs = []
        prev_y = events[0][0]
        total = 0
        areas = []

        def union_len(intervals):
            intervals.sort()
            res = cur = 0
            end = -10**30
            for a, b in intervals:
                if a > end:
                    res += b - a
                    end = b
                elif b > end:
                    res += b - end
                    end = b
            return res

        for y, typ, x1, x2 in events:
            if y > prev_y and xs:
                h = y - prev_y
                w = union_len(xs)
                areas.append((prev_y, h, w))
                total += h * w
            if typ == 1:
                xs.append((x1, x2))
            else:
                xs.remove((x1, x2))
            prev_y = y

        half = total / 2
        acc = 0
        for y, h, w in areas:
            if acc + h * w >= half:
                return y + (half - acc) / w
            acc += h * w

        return 0.0
        