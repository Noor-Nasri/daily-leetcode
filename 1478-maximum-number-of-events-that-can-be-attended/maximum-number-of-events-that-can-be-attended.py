from heapq import heappop, heappush
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events = sorted(events, reverse = True)
        numEvents = 0
        avail = []

        for day in range(1, 10**5 + 1):
            # First keep track of all events now open, then take whichever ends soonest
            while events and events[-1][0] == day:
                heappush(avail, events[-1][1])
                events.pop()
            
            while avail and day > avail[0]:
                heappop(avail)
            
            if avail:
                # There is an event available for this day
                heappop(avail)
                numEvents += 1

        return numEvents