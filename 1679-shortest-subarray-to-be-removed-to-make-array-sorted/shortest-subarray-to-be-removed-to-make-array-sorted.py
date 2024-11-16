class Solution:
    def bestIncluding0(self, arr):
        right_side = [arr[-1]]
        for ind in range(len(arr) - 2, -1, -1):
            if arr[ind] <= arr[ind + 1]:
                right_side.append(arr[ind])
            else:
                break
        if len(right_side) == len(arr): return 0

        # Now we have latest non-dec sequence of [y, n]
        # We consider [0, x] for x in 0->n. At each point, we try to merge with [y, n]
        best = len(arr)
        for ind in range(len(arr) - 1):
            if ind and arr[ind] < arr[ind - 1]:
                break 
            
            # consider: [0, ind] and right_side
            while right_side and arr[ind] > right_side[-1]:
                right_side.pop()
            
            option = len(arr) - len(right_side) - ind - 1
            if option < best:
                best = option
        
        #print(best)
        return best

    def bestIncludingN(self, arr):
        left_side = [arr[0]]
        for ind in range(1, len(arr)):
            if arr[ind] >= arr[ind - 1]:
                left_side.append(arr[ind])
            else:
                break

        if len(left_side) == len(arr): return 0
        #print(left_side)

        # Now we have earliest non-dec sequence of [0, x]
        # We consider [y, n] for y in n->0. At each point, we try to merge with [0, x]
        best = len(arr)
        for ind in range(len(arr) - 1, -1, -1):
            if ind < len(arr) - 1 and arr[ind] > arr[ind + 1]:
                break 
            
            # consider: [ind, n] and left_side
            while left_side and left_side[-1] > arr[ind]:
                left_side.pop()
            
            #print("Looking at option", left_side, arr[ind:])
            option = ind - len(left_side)
            #print("which means", arr[len(left_side):ind], "which is len", option)
            if option < best:
                best = option
        
        return best

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        return min(self.bestIncluding0(arr), self.bestIncludingN(arr))
        
        