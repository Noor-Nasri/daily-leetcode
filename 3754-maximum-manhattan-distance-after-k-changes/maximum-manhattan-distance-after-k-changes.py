class Solution:
    def getDistAndNumToSwitch(self, occur1, occur2):
        dist = abs(occur1 - occur2)
        numSwitch = min(occur1, occur2)
        return dist, numSwitch

    def maxDistance(self, s: str, k: int) -> int:
        counts = {"N": 0, "S": 0, "E": 0, "W":0}
        maxDist = 0
        for c in s:
            counts[c] += 1
            
            # if we change up to k prev, how far can be end up?
            d1, ns1 = self.getDistAndNumToSwitch(counts["N"], counts["S"])
            d2, ns2 = self.getDistAndNumToSwitch(counts["E"], counts["W"])
            dist = d1 + d2 +  2 * min(ns1 + ns2, k)
            maxDist = max(maxDist, dist)

        return maxDist