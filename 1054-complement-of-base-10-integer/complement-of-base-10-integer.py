class Solution:
    def bitwiseComplement(self, n: int) -> int:
        curDigits = list(str(bin(n))[2:])
        newDigits = [str(1 - int(e)) for e in curDigits]
        newBinary = "".join(newDigits)
        return int(newBinary, 2)
        