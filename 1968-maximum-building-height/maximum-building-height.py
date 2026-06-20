class Solution:
    # Ideally we would just raise by 1 each time, but we will get limited by the restrictions
    # The greedy approach would be to raise just enough for the upcoming limit, but maybe we cant lower in time
    # My first instinct is binary search but verifying is probably the same as just solving this ..

    # Maybe we lower restrictions to be real limits. Eg: [[1, 10], [2, 2]] means the real limit at 1 is 3.
    # Then once limits are proper, we just go in order and maximize our height at every step. h = min(limit, last + dist)
    # So the real question is, how can we lower limits to account for future limits being even stricter?
    # We can just do a backwards loop! When we reach a restriction, we know the next one is valid. So just min(limit, nextLimit + diff)

    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions = sorted(restrictions)

        # Step 1: Make all limits true to future restrictions. 
        for ind in range(len(restrictions) - 2, -1, -1):
            curLimit = restrictions[ind][1]
            nextLimit = restrictions[ind + 1][1]
            delta = restrictions[ind + 1][0] - restrictions[ind][0]
            restrictions[ind][1] = min(curLimit, nextLimit + delta)
        
        # Step 2: Get as close to each limit as possible while jumping as high as you can in middle
        curHeight = 0
        maxHeight = 0
        lastId = 1
        for curId, newLimit in restrictions:
            middleSlots = curId - lastId - 1
            if curHeight + middleSlots <= newLimit: # Just go up as much as we can till next limit
                curHeight = min(newLimit, curHeight + middleSlots + 1)
                maxReach = curHeight

            elif newLimit < curHeight: # Go up at start, then down until the required limit
                requiredReduction = curHeight - newLimit - 1
                freeSlots = middleSlots - requiredReduction
                maxReach = curHeight + freeSlots // 2
                curHeight = newLimit

            else: # Go up to limit + 1, then go even higher up and back down to limit + 1
                desiredRaise = newLimit - curHeight + 1
                freeSlots = middleSlots - desiredRaise
                maxReach = newLimit + 1 + freeSlots // 2
                maxHeight = max(maxHeight, maxReach)
                curHeight = newLimit


            maxHeight = max(maxHeight, maxReach)
            lastId = curId
        
        # Step 3: Keep going to the moon
        curHeight += n - lastId
        maxHeight = max(maxHeight, curHeight)
        return maxHeight
