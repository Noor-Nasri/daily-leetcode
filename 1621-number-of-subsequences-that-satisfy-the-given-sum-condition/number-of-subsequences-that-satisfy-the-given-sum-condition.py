class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # 2 pointer, but they start at opposite ends. When the e is too big, it'll be too big for everyone.
        # When s and e can make target, we can pair s with any other value <= e and allow any number of elements inbetween
        # So for example, 5 numbers means we have: 1 (just s) + 1 (s and next) + 2 (middle yes/no) + 4 + 8 = 16 = 2^5
        nums = sorted(nums)
        s = 0
        e = len(nums) - 1
        combos = 0

        while s <= e:
            while nums[s] + nums[e] > target:
                e -= 1
                if s > e:
                    break
            else:
                combos += (2 ** (e - s)) % (10**9 + 7)
                combos %= (10**9 + 7)
                s += 1

        return combos