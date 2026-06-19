class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curAlt = 0
        maxAlt = 0
        for delta in gain:
            curAlt += delta
            maxAlt = max(maxAlt, curAlt)
        
        return maxAlt