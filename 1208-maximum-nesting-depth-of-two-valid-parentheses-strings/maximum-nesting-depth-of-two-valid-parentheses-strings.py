class Solution:
    # Okay this is way too complicated but essentially we get a bunch of brackets
    # We then choose any way to re-arrange them into 2 groups, just keeping relative ordering
    # We then want to minimize the two groups, ie max(depthA, depthB) is min.

    # So ideally the depth is 1: ()()()..() for both groups.
    # Unfortunately if we get ((())), we cant avoid one group getting the first 2 ( together.
    # So I think this is a simply greedy: Assign each open bracket to the smaller group. Pop the larger.

    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        maxDepth = 0
        depths = [0, 0]
        chosen = [None for i in range(len(seq))]
        for ind in range(len(seq)):
            largerDepthInd = int(depths[1] >= depths[0])
            if seq[ind] == "(":
                chosen[ind] = 1 - largerDepthInd
                depths[chosen[ind]] += 1
                maxDepth = max(maxDepth, max(depths))
            else:
                chosen[ind] = largerDepthInd
                depths[chosen[ind]] -= 1

        return chosen
