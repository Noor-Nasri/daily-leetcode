class Solution:
    # We can boil this down to a simple question. At a given day, whats the best lake to dry?
    # Its only worth it to dry a lake that is already full. Whichever lake will get flooded first, needs to be dried eventually
    # So we may as well just dry it right then!

    # So at a given point, we need to know which full-lake is going to be flooded the earliest
    def avoidFlood(self, rains: List[int]) -> List[int]:
        lakeToRainDays = {} # rain days are in descending order so we can pop earliest days
        standInLake = 0 # just a lake to use when its all dry
        for day in range(len(rains) - 1, -1, -1):
            lake = rains[day]
            if lake == 0:
                continue
            standInLake = lake 
            if lake not in lakeToRainDays:
                lakeToRainDays[lake] = []
            
            lakeToRainDays[lake].append(day)
        
        # now go forward, and dry as possible
        fullLakes = set()
        floodQueue = []
        choices = []
        for lake in rains:
            if lake == 0:
                if floodQueue:
                    _, nextFloodLake = heappop(floodQueue)
                    choices.append(nextFloodLake)
                    fullLakes.remove(nextFloodLake)
                else:
                    choices.append(standInLake)
            else:
                if lake not in fullLakes:
                    lakeToRainDays[lake].pop()
                    fullLakes.add(lake)
                    choices.append(-1)
                    if lakeToRainDays[lake]:
                        floodDate = lakeToRainDays[lake][-1]
                        heappush(floodQueue, (floodDate, lake))
                else:
                    return []
        
        return choices