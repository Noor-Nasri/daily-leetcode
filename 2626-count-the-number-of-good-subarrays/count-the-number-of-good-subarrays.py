class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # For each num, we get numOccur choose 2 to get number of pairs
        # Then we just have a classic sliding window

        numArrays = 0
        numOcurrances = {}
        curValidPairs = 0
        left = 0
        right = 0

        while right < len(nums):
            newVal = nums[right]
            if newVal not in numOcurrances:
                numOcurrances[newVal] = [1, 0]
            elif numOcurrances[newVal][0] == 1:
                numOcurrances[newVal] = [2, 1]
                curValidPairs += 1
            else:
                numOcurrances[newVal][0] += 1
                curValidPairs -= numOcurrances[newVal][1]
                numOcurrances[newVal][1] *= numOcurrances[newVal][0] / (numOcurrances[newVal][0] - 2)
                curValidPairs += numOcurrances[newVal][1]

            #print(numArrays, numOcurrances, curValidPairs)
            while curValidPairs >= k:
                numArrays += len(nums) - right
                oldVal = nums[left]
                if numOcurrances[oldVal][0] == 1:
                    del numOcurrances[oldVal]
                else:
                    curValidPairs -= numOcurrances[oldVal][1]
                    numOcurrances[oldVal][1] *= (numOcurrances[oldVal][0] - 2) / numOcurrances[oldVal][0]
                    curValidPairs += numOcurrances[oldVal][1]
                    numOcurrances[oldVal][0] -= 1

                #print("Pairs is now:", curValidPairs, "after incrementing numArrays to ", numArrays)
                left += 1

            
            right += 1 
            
        
        return numArrays