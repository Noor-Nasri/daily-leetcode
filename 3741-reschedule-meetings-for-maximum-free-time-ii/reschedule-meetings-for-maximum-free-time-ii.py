class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        # For each ind, its only useful if we can move it out of the current range
        # So, if we move it, the max duration is start[ind + 1] - end[ind - 1]
        # To move it, there needs to be a gap >= duration either before ind-1 or after ind+1

        #       0 [1, 4] [7, 9], [14, 16], [17, 20] 22
        # Gaps: 1,      3,      5,        1,        2
        # MaxBefore: 1,    3,        5,        5
        # MaxAfter:  5     5,        2,        2

        gaps = []
        for ind in range(len(startTime) + 1):
            prevEd = (ind > 0) and endTime[ind - 1] or 0
            curSt = (ind == len(startTime)) and eventTime or startTime[ind]
            #print(ind, prevEd, curSt)
            gaps.append(curSt - prevEd)
        #print(gaps)

        maxGapBeforeMeetingStart = [0 for i in range(len(startTime))]
        maxGapAfterMeetingEnd = [0 for i in range(len(startTime))]
        for ind in range(len(startTime)):
            rInd = len(startTime) - 1 - ind
            maxGapBeforeMeetingStart[ind] = max(gaps[ind], ind and maxGapBeforeMeetingStart[ind - 1] or 0)
            maxGapAfterMeetingEnd[rInd] = max(gaps[rInd + 1], ind and maxGapAfterMeetingEnd[rInd + 1] or 0)

        #print(maxGapBeforeMeetingStart)
        #print(maxGapAfterMeetingEnd)

        maxPossibleGap = max(gaps)
        for ind in range(len(startTime)):
            curDuration = endTime[ind] - startTime[ind]
            possibleToMove = False

            if ind and maxGapBeforeMeetingStart[ind - 1] >= curDuration:
                possibleToMove = True
            elif ind < len(startTime) - 1 and maxGapAfterMeetingEnd[ind + 1] >= curDuration:
                possibleToMove = True

            prevEd = ind and endTime[ind - 1] or 0
            nextSt = (ind < len(startTime) - 1) and startTime[ind + 1] or eventTime
            fullGap = nextSt - prevEd
            #print("Looking at moving", ind, " - the maximal gap is", fullGap, possibleToMove, curDuration)
            if not possibleToMove:
                fullGap -= curDuration
                # we can just shift it to the end

            maxPossibleGap = max(maxPossibleGap, fullGap)
            

        return maxPossibleGap


