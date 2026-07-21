class Solution:
    # We essentially have a bunch of active/inactive values and want max(sum(active))
    # We have two possible tactics:
    # 1) Find [inactive, active = x, inactive] and non-overlapping [active, inactive = y, active]
    #     --> Flip x to inactive and y to active. Bonus = y - x
    # 2) Find [active, inactive=x, active, inactive=y, active ]
    #    ---> Flip inner to inactive, then all 3 to active. Bonus = x + y

    # HOLDDD on, after typing out the DP I realized something .. we always do strategy 2!
    # Strategy 1 means we take (val1 - val2)
    # But val1 WILL be in the form of [inactive, active=prev, val1, active, inactive]
    # So we can do: flip prev, then flip both prev + val1 back to active
    # Then we get bonus = val1 > val1-val2

    # So the optimal move is always to flip then unflip the same area. Never segmented. 
    # So just do a single sweep to figure out bonus of flipping each ind

    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        origArray = [int(e) for e in s]
        activeArray = []
        countArray = []

        curActive, curCount = origArray[0], 1
        for ind in range(1, len(s)):
            if origArray[ind] == curActive:
                curCount += 1
            else:
                countArray.append(curCount)
                activeArray.append(curActive)
                curActive = origArray[ind]
                curCount = 1

        countArray.append(curCount)
        activeArray.append(curActive)

        maxBonus = 0
        for ind in range(1, len(activeArray) - 1):
            if activeArray[ind] and not activeArray[ind - 1] and not activeArray[ind + 1]:
                maxBonus = max(maxBonus,  countArray[ind - 1] + countArray[ind + 1])

        return sum(origArray) + maxBonus