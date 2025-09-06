class Solution:
    # Greedy approach would just take the biggest val possible, but that might lead to -1.
    # A DP approach would decide count of each val, but we memoize num1 which is 10^9.
    # How about BS on allowed operations? If we have a limit on allowed operations, we can do early pruning ?
    
    # If we decide on the exact # of operations, it becomes easier because we can just take num2 out and need to make the rest with powers of 2
    # Easy! But that is O(num operations). What is the upper limit on the number of operations we do ..?
    # The biggest possible number is 2 * 10^9, which has ~ 30 binary digits so we really should never need more than that many powers of 2.


    def canValBeExactlyXPowersOfTwo(self, val, x):
        # 9 only needs 2 ( 8 + 1), but can also be 3 ( 4 + 4 + 1), or 4 ( 4 + 2 + 2 + 1)
        # But 9 cannot take more than 9 1's. So the range is [numOnesInBin, val]
        numOnes = str(bin(val)).count('1')
        return numOnes <= x <= val


    def makeTheIntegerZero(self, num1: int, num2: int) -> int:

        curVal = num1
        for numOperations in range(1, 50):
            curVal -= num2
            if self.canValBeExactlyXPowersOfTwo(curVal, numOperations):
                return numOperations

        return -1
        