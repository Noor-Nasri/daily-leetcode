class Solution:
    # Wait, can we pick the same element twice?
    # Why wouldn't we just always close the biggest gap, ie store diffs in heap?
    # oh lol k is huge, so we need to figure out how much we can give each value
    # We can just sweep, minimizing all previous diffs to cur diff then expanding the group

    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diffs = sorted([abs(nums1[i] - nums2[i]) for i in range(len(nums1))], reverse = True) + [0]
        remainingAdjustments = k1 + k2

        #print("Initial diffs:", diffs)
        for ind in range(len(diffs) - 1):
            requiredAdjustments = (ind + 1) * (diffs[ind] - diffs[ind + 1])
            if requiredAdjustments <= remainingAdjustments:
                # Now all diffs until ind match [ind + 1]
                remainingAdjustments -= requiredAdjustments
                #print("At", ind, "=", diffs[ind], "we are down to", remainingAdjustments, "changes to continue")
            else:
                # Minimize all values <= ind, wont change remaining
                baseline = diffs[ind]
                #print("We will limit adjustments until", ind, " for baseline", baseline)

                if remainingAdjustments:
                    maxUnifiedAdjustment = remainingAdjustments // (ind + 1)
                    remainingAdjustments -= (ind + 1) * maxUnifiedAdjustment
                    baseline -= maxUnifiedAdjustment
                    #print("We've reduced baseline to", baseline)
                
                #print("Remaining adjustments:", remainingAdjustments)

                section1 = (baseline ** 2) * (ind + 1 - remainingAdjustments)
                section2 = ((baseline - 1) ** 2) * remainingAdjustments
                section3 = sum([e**2 for e in diffs[ind + 1:]])
                return section1 + section2 + section3

        # Managed to set everything to 0
        return 0
