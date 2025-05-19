class Solution:
    def triangleType(self, nums: List[int]) -> str:
        abc = sorted(nums)
        if abc[2] >= abc[0] + abc[1]:
            return "none"

        numEq = len(set(nums))
        names = ["equilateral", "isosceles", "scalene"]
        return names[numEq - 1]
        