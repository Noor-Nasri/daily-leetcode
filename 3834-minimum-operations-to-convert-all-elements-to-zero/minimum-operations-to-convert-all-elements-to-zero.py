class Solution:
    # I was thinking of going min to max and tracking zero inds, but this might be troublesome because how do I update the zero inds?
    # Is it possible to think of this in one go? As I iterate, each number gets put in some stack. 
    # When I see a smaller value, all bigger values so far would have eventually gotten zerod out later.
    # Thinking backwards can work! If the ideal strategy is to zero from min-to-max, then I can also start with just segmenting off max
    # vex: 1, 5, 2 --> [1, 5] in stack, then 2 means [5] is one segment and would get zeroes out later. Now [1, 2] and 1, 0 shows up
    # When we get the 1, we know [2] is alone. Then we have [1, 1] and 0 says the 2 1s are goneza

    def minOperations(self, nums: List[int]) -> int:
        numOperations = 0
        curStack = []
        for val in nums:
            while curStack and val < curStack[-1]:
                # The prev value is isolated anyways. Figure out its segment, and that will be zeroes out at the *end*, but we count it now!
                prevVal = curStack[-1]
                numOperations += 1
                while curStack and prevVal == curStack[-1]:
                    curStack.pop()

            if val:
                curStack.append(val)

        while curStack:
            # Already finished, so go back on increasing subarrs and zero them out
            prevVal = curStack[-1]
            numOperations += 1
            while curStack and prevVal == curStack[-1]:
                curStack.pop()
        return numOperations
        