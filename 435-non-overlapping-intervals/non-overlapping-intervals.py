class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Alternatively: max # of non overlapping meetings.
        # Cant we just keep taking earliest end date?
        numTaken = 0
        intervals = sorted(intervals, key = lambda x : x[1])
        acceptableStart = float('-inf')
        for s, e in intervals:
            if s >= acceptableStart:
                acceptableStart = e
                numTaken += 1
        
        return len(intervals) - numTaken
        