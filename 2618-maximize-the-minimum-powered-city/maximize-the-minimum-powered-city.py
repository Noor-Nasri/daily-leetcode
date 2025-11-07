class Solution:
    # This looks like a straight forward BS with a lengthy implementation
    # If we set the min power to x, we then go from left to right and add stations as far right as possible, when needed
    # If we run out of towers, then we cannot achieve that min. 
    # We just need to start with some prefix sums to account for the ranges

    def canMakeAllCitiesHaveXPower(self, stationPowers, desiredPower, towerRange, remTowers):
        additionalPowerCutoffs = {}
        additionalPower = 0
        for ind in range(len(stationPowers)):
            additionalPower -= additionalPowerCutoffs.get(ind, 0)
            curPower = stationPowers[ind] + additionalPower
            if curPower >= desiredPower:
                continue
            
            needed = desiredPower - curPower
            if needed > remTowers:
                return False
            
            additionalPower += needed
            remTowers -= needed
            towerCutoff = ind + towerRange * 2 + 1 # The tower gets placed at i + k, and reaches another k. Then we cutoff
            additionalPowerCutoffs[towerCutoff] = needed

        return True


    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        stationPowers = [0 for i in range(len(stations))]
        for ind in range(len(stations)):
            stationPowers[max(ind - r, 0)] += stations[ind]
            if ind + r + 1 < len(stations):
                stationPowers[ind + r + 1] -= stations[ind]
        for ind in range(1, len(stations)):
            stationPowers[ind] += stationPowers[ind - 1]
        
        low = min(stationPowers)
        high = max(stationPowers) + k 
        best = low

        while low <= high:
            mid = (low + high) // 2
            if self.canMakeAllCitiesHaveXPower(stationPowers, mid, r, k):
                best = mid
                low = mid + 1
            else:
                high = mid -1 

        return best
        