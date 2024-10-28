class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        longestStreak = -1
        possibleSqaures = {}
        nums = sorted(nums)

        for value in nums:
            sqrt = value ** 0.5
            if sqrt in possibleSqaures:
                possibleSqaures[value] = possibleSqaures[sqrt] + 1
                longestStreak = max(longestStreak, possibleSqaures[value])
            else:
                possibleSqaures[value] = 1


        return longestStreak


        