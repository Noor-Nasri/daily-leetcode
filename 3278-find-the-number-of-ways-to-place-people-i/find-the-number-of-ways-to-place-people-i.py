class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # I first misread this as a choosing max combos. We just want to look at every pair and know if anything is within the rect
        # So, if for each X, we go backwards through previous points, then we can maintain which rects have been seen.
        # Eg. (1, 5), (2, 0) means we have a 1x5 rect here. If (0, 10) was before, it would overlap.
        
        # I feel like there is some clever nlogn here, but n^3 will pass so I'll just do it and move on
        points = sorted(points, key = lambda e : e[0] * 51 - e[1]) # For same X, go big Ys first so they can be the A
        found = 0

        for indB in range(len(points)):
            _, By = points[indB]
            for indA in range(indB - 1, -1, -1):
                _, Ay = points[indA]
                if Ay < By:
                    continue
                
                valid = True
                for indMiddle in range(indA + 1, indB):
                    _, My = points[indMiddle]
                    if By <= My <= Ay:
                        valid = False
                        break
                
                if valid:
                    found += 1
        
        return found