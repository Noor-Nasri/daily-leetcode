from heapq import heapify, heappush, heappop

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        availableChairs = [i for i in range(len(times))]
        usedChairs = []
        heapify(availableChairs)

        target_start_time = times[targetFriend][0]
        times = sorted(times)

        for st, en in times:
            while usedChairs and st >= usedChairs[0][0]:
                old_en, old_chair = heappop(usedChairs)
                heappush(availableChairs, old_chair)
            
            newChair = heappop(availableChairs)
            if st == target_start_time:
                return newChair

            heappush(usedChairs, (en, newChair))


        assert False