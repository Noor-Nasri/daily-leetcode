class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right: return left
        bits1 = list(bin(left))
        bits2 = list(bin(right))

        if len(bits2) > len(bits1):
            # Will just be 1000..00 AND 00xx..x = 00..00 
            return 0

        total = 0
        ind = 2

        while ind < len(bits1):
            if bits1[ind] == '0' and bits2[ind] == '0':
                # Wont touch this one, but rest may match up
                ind += 1
                continue
            elif bits1[ind] == '0' or bits2[ind] == '0':
                # Rest will all be 0s
                return total
            
            total += 2 ** (len(bits1) - ind - 1)
            ind += 1


        return total
        