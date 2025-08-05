from collections import deque
from heapq import heapify, heappop, heappush

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Just a normal heap question: before each meeting, free up any rooms then give it the lowest number
        # If it cannot be matched, then put it in a queue: when we free up rooms, we first look in this queue
        # At the end, just get the room with most meetings.
        meetings = sorted(meetings)
        availableRooms = [i for i in range(n)]
        usedRooms = [] # (availTime, room)
        lateMeetings = deque() # duration of meeting that was supposed to start already, in order of start time
        meetingCounts = {i: 0 for i in range(n)}

        for s, e in meetings:
            # Before this meeting starts, figure out which rooms became available
            while usedRooms and usedRooms[0][0] <= s:
                availTime, room = heappop(usedRooms)
                # if a meeting hasn't started yet, it would have gotten this room
                if lateMeetings:
                    duration = lateMeetings.popleft()
                    meetingCounts[room] += 1
                    heappush(usedRooms, (availTime + duration, room))
                else:
                    heappush(availableRooms, room)

            # now Process this room
            if availableRooms:
                bestRoom = heappop(availableRooms)
                meetingCounts[bestRoom] += 1
                heappush(usedRooms, (e, bestRoom))
            else:
                lateMeetings.append(e - s)
        

        # Still need to process any late meetings, meaning all rooms are used
        while len(lateMeetings):
            availTime, room = heappop(usedRooms)
            duration = lateMeetings.popleft()
            meetingCounts[room] += 1
            heappush(usedRooms, (availTime + duration, room))
        
        # Now finish
        bestRoom = 0
        for i in range(n):
            if meetingCounts[i] > meetingCounts[bestRoom]:
                bestRoom = i
        
        return bestRoom



        


