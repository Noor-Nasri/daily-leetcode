class Solution:
    def canXCandiesBeDistributed(self, candies, k, x):
        for val in candies:
            numFed = val // x
            k -= numFed

            if k <= 0:
                return True
        
        return False

    def maximumCandies(self, candies: List[int], k: int) -> int:
        # Could be solved with binary search on num candies --> log(10^7) * 10^5
        # can store how many children can be fed for each candy[i] value --> 10^7 array, or 10^5 hashmap
        low = 1
        high = max(candies)
        best = 0

        while low <= high:
            mid = (low + high) // 2
            valid = self.canXCandiesBeDistributed(candies, k, mid)
            if valid:
                best = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return best