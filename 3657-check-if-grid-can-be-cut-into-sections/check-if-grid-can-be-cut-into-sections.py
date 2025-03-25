class Solution:
    def checkCutsAlongAxis(self, rectangles, axis):
        # axis 0 means sort by x and split vertical, axis 1 means sort by y and split horizonal
        rectangles = sorted(rectangles, key = lambda x: x[axis])
        numSections = 0
        curSectionEnd = -1

        for BL_X, BL_Y, TR_X, TR_Y in rectangles:
            if axis == 0:
                start, end = BL_X, TR_X
            else:
                start, end = BL_Y, TR_Y


            if start < curSectionEnd:
                curSectionEnd = max(curSectionEnd, end)
            else:
                numSections += 1
                curSectionEnd = end

                if numSections == 3:
                    return True

        return False


    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        return self.checkCutsAlongAxis(rectangles, 0) or self.checkCutsAlongAxis(rectangles, 1)
        