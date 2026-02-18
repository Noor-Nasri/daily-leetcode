class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        st = str(bin(n))[2:]
        for ind in range(1, len(st)):
            if st[ind] == st[ind-1]:
                return False
        
        return True
        