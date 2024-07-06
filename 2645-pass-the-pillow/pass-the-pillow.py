class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        fullRotations = time // (2*n - 2)
        time -= fullRotations * (2*n - 2)

        # now at pos 0 with time
        if time < n:
            return time + 1
        else:
            time -= n - 1
            ans = n - time
            return ans
        