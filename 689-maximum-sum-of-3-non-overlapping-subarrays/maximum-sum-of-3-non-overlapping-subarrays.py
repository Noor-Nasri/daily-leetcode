class Solution:
    def extractInd(self, exactSolutions, bestSolutionSinceInd, ind_arr, allowed_start):
        best_score = bestSolutionSinceInd[ind_arr][allowed_start]
        for ind_element in range(allowed_start, len(exactSolutions[ind_arr])):
            if exactSolutions[ind_arr][ind_element] == best_score:
                return ind_element


    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        prefixSums = [0]
        for num in nums:
            prefixSums.append(prefixSums[-1] + num)
        
        exactSolutions = [
            [0 for i in range(len(nums))]
            for e in range(3)
        ]

        bestSolutionSinceInd = [
            [0 for i in range(len(nums))]
            for e in range(3)
        ]

        for ind_arr in range(2, -1, -1):
            bestScore = -1
            for ind_element in range(len(nums) - (3 - ind_arr)*k, -1, -1):
                score = prefixSums[ind_element + k] - prefixSums[ind_element]
                if ind_arr < 2:
                    score += bestSolutionSinceInd[ind_arr + 1][ind_element + k]
                bestScore = max(bestScore, score)

                exactSolutions[ind_arr][ind_element] = score
                bestSolutionSinceInd[ind_arr][ind_element] = bestScore


        # now construct the answer
        ind1 = self.extractInd(exactSolutions, bestSolutionSinceInd, 0, 0)
        ind2 = self.extractInd(exactSolutions, bestSolutionSinceInd, 1, ind1 + k)
        ind3 = self.extractInd(exactSolutions, bestSolutionSinceInd, 2, ind2 + k)
        return [ind1, ind2, ind3]
        