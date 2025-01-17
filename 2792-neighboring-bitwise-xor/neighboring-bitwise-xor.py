class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # start with [a, b, c]
        # results in [x = a xor b, y = b xor c, z = c xor a]
        # xor entire result should then give 0

        tot = 0
        for num in derived:
            tot ^= num
        
        return tot == 0
        
        