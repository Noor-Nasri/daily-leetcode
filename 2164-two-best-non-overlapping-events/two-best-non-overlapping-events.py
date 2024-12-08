class Solution:
    def binSearch(self, event_two_choices, s):
        low = 0
        high = len(event_two_choices) - 1
        best = 0

        while low <= high:
            mid = (low + high) // 2
            if event_two_choices[mid][0] > s:
                best = event_two_choices[mid][1]
                high = mid - 1
            else:
                low = mid + 1

        return best

    

    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Idea: choose event1, and then event2 is just maximum possible
        # Issue: cannot use time <= 10^9. 

        event_two_choices = []
        # only keep early events if they are strictly better
        best = 0
        for s,e,v in sorted(events, reverse = True):
            if v > best:
                event_two_choices.append((s, v))
                best = v
        
        event_two_choices = event_two_choices[::-1]

        maxVal = 0
        for s, e, v in events:
            # best pair is earliest start > s in event_two_choices, since it has max value
            val = v + self.binSearch(event_two_choices, e)
            maxVal = max(maxVal, val)

        return maxVal
        