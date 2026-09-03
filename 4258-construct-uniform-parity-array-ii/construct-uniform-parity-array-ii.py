class Solution:
    # To convert even to odd: Just pick an odd pairing for every even number.
    # Meaning every even number needs a *smaller* odd number. So true iff min(vals) is odd.
    # To convert odd to even: need to subtract another odd. But what about the smallest odd?
    
    # So then the solution is just: All even, all odd, or min(vals) is odd.
    # Is that all? Is this really medium?

    def uniformArray(self, nums1: list[int]) -> bool:
        parityExists = [0, 0]
        minVal = 10**10
        for num in nums1:
            parityExists[num % 2] = 1
            minVal = min(minVal, num)
        
        return (sum(parityExists) == 1 or minVal % 2 == 1)