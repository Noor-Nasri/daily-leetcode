class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        largest = 0;

        while (numbers):
            chain_start = numbers.pop()

            count = 1
            cur = chain_start - 1
            while (cur in numbers):
                numbers.remove(cur)
                cur -= 1
                count += 1
            
            cur = chain_start + 1
            while (cur in numbers):
                numbers.remove(cur)
                cur += 1
                count += 1
            
            if count > largest:
                largest = count

        return largest

