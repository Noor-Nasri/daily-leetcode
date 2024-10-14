from heapq import heapify, heappush, heappop
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        pq = [-e for e in nums]
        heapify(pq)

        total = 0
        for i in range(k):
            val = heappop(pq)
            total += -val
            heappush(pq, math.floor(val/3))

        return total
        