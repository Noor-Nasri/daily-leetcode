class Solution:
    def setToTarget(self, digits, target):
        chosen = None
        for i in range(len(digits)):
            if digits[i] == target:
                continue
            
            if not chosen or chosen == digits[i]:
                chosen = digits[i]
                digits[i] = target
        
        return int("".join(digits))

    def minMaxDifference(self, num: int) -> int:
        digits = list(str(num))
        maxNum = self.setToTarget(digits[:], '9')
        minNum = self.setToTarget(digits[:], '0')
        return maxNum - minNum