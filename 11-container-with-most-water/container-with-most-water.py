class Solution:
    # As we see new lines, we can maintain the best starting point to use for the future
    # If we see a point lower than the previous ones, it's obviously better to just use the old point for A
    # In that case, we maintain an acesndending list to be used for (A, _) rects (limit 10^4 instead of 10^5)
    # We can do the same idea for the best B elements and maintain (_, B), then merging these lists should solve in time ..

    # Can we incorporate some binary search or smarter filtering? Maybe 2 pointer?
    # Yes, 2 pointer! If we start with widest (A, B), and A is the shorter one, it is the limiting factor and already max length. 
    # So just go to next A! Then its O(n)

    def maxArea(self, height: List[int]) -> int:
        viableAInds = [0]
        for ind in range(1, len(height)):
            if height[ind] > height[viableAInds[-1]]:
                viableAInds.append(ind)
        
        viableBInds = [len(height) - 1]
        for ind in range(len(height) -1, -1, -1):
            if height[ind] > height[viableBInds[-1]]:
                viableBInds.append(ind)
        
        maxWater = 0
        curIterA = 0
        curIterB = 0
        while curIterA < len(viableAInds) and curIterB < len(viableBInds):
            indA, indB = viableAInds[curIterA], viableBInds[curIterB]
            if indA >= indB:
                break

            hA, hB = height[indA], height[indB]
            area = min(hA, hB) * (indB - indA)
            maxWater = max(maxWater, area)

            if hA <= hB:
                curIterA += 1
            if hB <= hA:
                curIterB += 1
            


        return maxWater
