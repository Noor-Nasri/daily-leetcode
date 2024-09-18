import functools

def compare(a, b):
    num1 = int(a + b)
    num2 = int(b + a)
    if num1 > num2:
        return -1
    elif num1 < num2:
        return 1
    return 0

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if sum(nums) == 0:
            return "0"

        return "".join(sorted([str(e) for e in nums], key = functools.cmp_to_key(compare)))
        