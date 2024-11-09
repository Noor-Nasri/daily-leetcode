class Solution:
    def setToNthOffset(self, n):
        if n == 0: return
        numZeroes = 0
        ind = -1
        lastZero = -1

        while 2 ** numZeroes - 1 < n:
            ind += 1
            if ind == len(self.binList):
                self.binList.append('0')

            if self.binList[ind] == '0':
                numZeroes += 1
                lastZero = ind

        self.binList[lastZero] = '1'
        self.setToNthOffset(n - 2 ** (numZeroes - 1))


    def minEnd(self, n: int, x: int) -> int:
        # you must have x, cuz if any 1s are 0s it'll never be made.
        # then you keep making the smallest element by switching a 0 to 1
        # eg: 111 -> 1111 because we cannot make the original 1s 0
        # but 100 -> 101 -> 110 -> 111

        self.binList = list(str(bin(x)[2:]))[::-1] # flip so its easy to add a 1 to the start
        self.setToNthOffset(n - 1)
        result = int("".join(self.binList[::-1]), 2)
        return result

        