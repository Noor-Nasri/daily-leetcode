class Solution:
    # Okay so the list doesn't even matter, we have all values 1->n
    # Given n, how many numbers can you get by XORing three numbers in [1, n]
    # Wait, then we can literally just pick any number 3 times to include it.

    # So 1->n can all be made. Then values with a higher bit order than n cannot be included
    # Eg n = 1101 (binary) -> impossible to make 10000 (binary) or larger
    # So the real question is just: how many in [n, 1111..11] can be made?

    # Eg: n = 10010. So next value is 10011 -> how to immediately combine with (101 x 1)
    # So: For any value with >= 1 zero, we can just do: 1000..00 + remaining1s_andAdditional + revert_last
    # If the desired value is all 1s, then as long as its >= 3 bits, we can also just split it 
    # So what can't be made?? Maybe 10100 ? No, just take n -> xor with missing and back
    # Is this answer just everything within bit range??

    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
            
        numBits = int(log(n, 2))
        return 2 ** (numBits + 1)