from heapq import heappush, heappop

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # If only positives: classic 2 pointer, expand window until we have k then shrink as much as possible
        # But with negatives, we might be able to shrink even further so can't use linear pointer ..
        # After some hints: we simply do prefix sum, but instead of considering all starts to our end, only take highest sums

        seen = []
        bestLen = -1
        total = 0
        heappush(seen, (0, -1))

        for ind, val in enumerate(nums):
            total += val
            while seen and total - seen[0][0] >= k:
                option = ind - seen[0][1]
                if bestLen == -1 or option < bestLen:
                    bestLen = option
                heappop(seen) # If this ind is ever useful later, it wont ber bestLen anyways

            heappush(seen, (total, ind))
            
        return bestLen
        
        