class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        rightSum = sum(nums)
        leftSum = 0
        answer = []

        for num in nums:
            rightSum -= num
            answer.append(abs(rightSum - leftSum))
            leftSum += num
        
        return answer