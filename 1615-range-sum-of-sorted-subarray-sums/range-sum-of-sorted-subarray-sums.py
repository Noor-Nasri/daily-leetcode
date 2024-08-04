class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        tots = []
        for ind_s in range(n):
            tot = 0
            ind_e = ind_s

            while (ind_e < n):
                tot += nums[ind_e]
                tots.append(tot)
                ind_e += 1
        
        tots = sorted(tots)
        result = 0
        for ind in range(left - 1, right):
            result = (result + tots[ind]) % (10**9 + 7)

        return result

        