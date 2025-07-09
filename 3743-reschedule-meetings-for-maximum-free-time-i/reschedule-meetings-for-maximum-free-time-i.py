class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        # Biggest gap might be before or after events, or in middle of 2 events
        # With prefix sums, we can get duration of last k events and push them all back to the left
        # We can also do that for the right. But how do we know the optimal push between left and right?

        # Similar idea: instead of looking at each gap, look at every "group" of size k + 1. 
        # In that window, we can just shift the first k to the left. But is it okay to ignore smaller window sizes?
        # Yes because if the biggest gap is between i,j - shifting both to the left will give us that gap on the right.
        
        durationSums = [0]
        for ind in range(len(startTime)):
            duration = endTime[ind] - startTime[ind]
            durationSums.append(durationSums[-1] + duration)
        
        if k >= len(startTime):
            return eventTime - durationSums[-1]

        maxGap = 0
        for ind_gap in range(k - 1, len(startTime)):
            # If k = 2, then we start at ind_gap = 1 and consider shifting first 2 elements to left
            # Then our prevEnd is just 0, our next event is at [2], and we move (duration[2] - duration[0]) to the prevEvent

            prevEventEnd = 0
            if ind_gap - k >= 0:
                prevEventEnd = endTime[ind_gap - k]
            
            nextEventStart = eventTime
            if ind_gap < len(startTime) - 1:
                nextEventStart = startTime[ind_gap + 1]

            durationOfKEvents = durationSums[ind_gap + 1] - durationSums[ind_gap - k + 1]
            gap = nextEventStart - durationOfKEvents - prevEventEnd
            maxGap = max(maxGap, gap)
        
        return maxGap