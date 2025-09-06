class Solution:
    # 10^5 queries, each having an array length of 10^9. 
    # that being said, the array is just continous. Each value needs to be selected ~log(val, base=4) times.
    # For each query, we can do a BS variant to determine the different range values.
    # For example, if l takes 5 iterations to get to 0, we want to find the first ind that takes 6. Then 7, etc.
    # Even 10^9 only needs <15 iterations, so we are doing <= 15 binary search operations.
    
    # This got TLE.... Each binary search operation is log2(10^9) = ~30, and within each one we are doing log4
    # So in theory this is n(log2_x)(log4_x)^2 = 10^5 * 30 * 15^2 = ~600mil which does TLE.

    # Alternatively, we can just take the 15 basic ranges and check if they are in the range ... just 15n. LOL.

    def minOperations(self, queries: List[List[int]]) -> int:
        total = 0

        for low, high in queries:
            curVal = 1
            nOperations = 0
            for numDiv in range(1, 16):
                nextVal = curVal * 4

                rangeStart = max(low, curVal)
                rangeEnd = min(high + 1, nextVal)
                numIncluded = max(0, rangeEnd - rangeStart)
                #print("Range", rangeStart, rangeEnd, "includes", numIncluded, "at", numDiv, "operations")
                nOperations += numIncluded  * numDiv
                curVal = nextVal

            total += (nOperations + 1)//2

        return total
