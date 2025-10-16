class Solution:
    # My first intuition is to simply loop from 0 to 10^5 and check if the number can be made. But how?
    # Alternatively, we can go through the numbers in sorted order and put them in the smallest available spot for their remainder.
    # Actually, if we x values have remainder y, we know y, y + value, ... y + (x - 1)*value can all be made. So just count.

    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        remainderCounts = [0 for i in range(value)]
        for num in nums:
            remainderCounts[num % value] += 1
        
        smallestExclusions = [i + value*remainderCounts[i] for i in range(value)]
        return min(smallestExclusions)
