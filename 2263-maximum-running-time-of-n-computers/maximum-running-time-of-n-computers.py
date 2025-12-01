class Solution:
    # If you have an extra battery and leave it till the end, it might not get used cuz all the other batteries are dead
    # So we need distribute the cost amongst the batteries. At any given second, the top n batteries lose 1 life.
    # But how can we do this when they have 10^9 life? We can compute when the lowest in the group gets replaced? Then what about group of 3?
    # If we say ans = 10min, that means the last k batteries are put together to reach that time. 
    # That should be the answer. Just do BS and work backwards to match that time.

    def canReachTime(self, n, sortedBatteries, desiredTime):
        numFullyCharged = 0
        curChargingAbility = 0
        for battery in sortedBatteries:
            needed = desiredTime - curChargingAbility
            if battery < needed:
                curChargingAbility += battery
            else:
                # We are needed from time [curChargingAbility], so we cannot provide more than that
                curChargingAbility =  min(battery - needed, curChargingAbility)
                numFullyCharged += 1

        return numFullyCharged >= n

    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        sortedBatteries = sorted(batteries)
        low = 0
        high = round(sum([e/n for e in batteries])) + 1
        best = 0

        while low <= high:
            mid = (low + high)//2
            if self.canReachTime(n, sortedBatteries, mid):
                best = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return best
        