class Solution:
    # Find the smallest multiple of k that has form 11...1
    # So k*x = 10^i + 10^(i-1) + ... + 10 + 1
    # Simplest solution is to just try all values, but can we ever stop? Maybe like 100 ones? But that'll kill python
    # Can we just not sure the full number? Eg: 111 % 101 = 10. Now we want to test 1111 % 101, but without storing the 1111
    # (111 % 101) = 10  <--> ((111 % 101) * 10 + 1) % 101 = (10*10 + 1) % 101
    # ((111 % 101) * 10 + 1) % 101 = ... idk man I feel like we can just keep checking the remainder

    def smallestRepunitDivByK(self, k: int) -> int:
        if k == 1:
            return 1

        rem = 11 % k
        for i in range(10**6):
            if rem == 0:
                return i + 2
            rem = (rem * 10 + 1) % k

        return -1