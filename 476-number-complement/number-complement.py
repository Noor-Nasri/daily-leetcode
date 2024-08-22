class Solution:
    def findComplement(self, num: int) -> int:
        return int("".join([str(1 - int(e)) for e in str(bin(num)[2:])]), 2)
        