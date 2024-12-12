class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            m = max(gifts)
            ind = gifts.index(m)
            gifts[ind] = int(gifts[ind]**0.5)
        return int(sum(gifts))