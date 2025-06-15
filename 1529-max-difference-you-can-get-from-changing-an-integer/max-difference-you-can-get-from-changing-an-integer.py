class Solution:
    def swapFirstNonValToTarget(self, digits, startInd, targets):
        # kind of a messy generic func, could just have split it up
        # First letter not in targets will be swapped with targets[0]

        for ind in range(startInd, len(digits)):
            num = digits[ind]
            if num not in targets:
                target = targets[0]
                digits = [(target if e == num else e) for e in digits]
                break

        return int("".join(digits))
    
    def maxDiff(self, num: int) -> int:
        # For max: Change the first non-9 to a 9
        # For min: Change the first number to 1, or the first non-zero, non-one to 0
        digits = list(str(num))
        maxNum = self.swapFirstNonValToTarget(digits, 0, ["9"])

        if digits[0] == "1":
            minNum = self.swapFirstNonValToTarget(digits, 1, ["0", "1"])

        else:
            digits = [("1" if e == digits[0] else e) for e in digits]
            minNum = int("".join(digits))

        return maxNum - minNum