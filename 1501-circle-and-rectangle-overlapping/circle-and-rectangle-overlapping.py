class Solution:
    # Surely there is a simple O(1) math verification here.
    # Iif the circle midpoint is to the left/right/above/below, we just consider the diff on the unaligned axis
    # If its in the diagonal, ie both x and y are out of range, then it cant overlap without also touching the corner

    # So we just if: center is inside, or within r to corners, or if its within [x1, x2] and yDiff < r, or [y1, y2] and xDiff < r

    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if x1 <= xCenter <= x2 and y1 <= yCenter <= y2:
            return True    
        elif x1 <= xCenter <= x2:
            return min(abs(y1 - yCenter), abs(y2 - yCenter)) <= radius
        elif y1 <= yCenter <= y2:
            return min(abs(x1 - xCenter), abs(x2 - xCenter)) <= radius
        else:
            corners = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
            for x, y in corners:
                if (xCenter - x) ** 2 + (yCenter - y) ** 2 <= radius ** 2:
                    return True
        
        return False