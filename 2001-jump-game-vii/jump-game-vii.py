class Solution:
    # Basic graph traversal but even simpler since we never go backwards
    # So at each 0, we want to know if a validated 0 exists min->max jumps prior.
    # If yes, then this 0 is also validated/reachable, and useful for future points

    # If we track all 0 inds, then get the earliest ind >= max cutoff (binary search)
    # Then we can just check if its within <= minCutoff. So O(nlogn) overall

    def getLargestValSmallerEqCutoff(self, inds, maxValue):
        low = 0
        high = len(inds) - 1
        best = -1

        while (low <= high):
            mid = (low + high)//2
            if inds[mid] <= maxValue:
                best = inds[mid]
                low = mid + 1
            else:
                high = mid - 1

        return best

    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        reachable = [0]
        for ind in range(1, len(s)):
            if s[ind] == "1":
                continue

            prevInd = self.getLargestValSmallerEqCutoff(reachable, ind - minJump)
            if prevInd >= max(0, ind - maxJump):
                reachable.append(ind)

        return  reachable[-1] == len(s)-1
    