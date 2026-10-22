class Solution:
    # S moves first element to last. R flips the array
    # RSR means we move the last element to the first.
    # SRS just ends up the same as a single R.
    # Anyways, before we can explore some traversal or DP we need to consider the problem space
    # Given the starting permute, can we achieve all permutes?
    # NO: Noes can ever escape neighbours. We just shift the start or flip dir, but the chain is always the same

    # So all we need to do is make 0 and 1 at positions [0] and [1], and see if the rest of the chain is in place.

    # BRO I am on like submission 192, so many edge case garbages

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        elif n == 2:
            return 0 if nums == [0, 1] else 1

        initPos0 = -1
        initIsBackwards = False

        for ind in range(n):
            val = nums[ind]
            before = nums[(ind - 1) % n]
            after = nums[(ind + 1) % n]
            adjs = [min(before, after), max(before, after)]
            expectedAdj = [val - 1, val + 1]

            if val == 0:
                initPos0 = ind
                expectedAdj = [1, n - 1]
            elif val == 1 and initPos0 == -1:
                initIsBackwards = True
            elif val == n - 1:
                expectedAdj = [0, n - 2]

            if adjs != expectedAdj:
                return -1 

        # Edge case: starting on loop ends, makes generic dir logic break
        if nums[0] == 0:
            initIsBackwards = nums[-1] == 1
        elif nums[-1] == 0:
            initIsBackwards = nums[-2] == 1

        
        # The whole chain is valid, now just need to slide (0, 1) into [0], [1]
        options = []

        # Move all the way left
        if initIsBackwards:
            flippedPos0 = n - 1 - initPos0
            options.append(1 + flippedPos0)
        else:
            options.append(initPos0)
        
        # Move left until we loop as ..210, then flip again. 
        if initIsBackwards:
            options.append(initPos0 + 2)
        else:
            flippedPos0 = n - 1 - initPos0
            options.append(flippedPos0 + 3)
        
        return min(options)





        