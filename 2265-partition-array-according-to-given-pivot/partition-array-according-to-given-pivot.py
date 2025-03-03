class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        arr1 = []
        arr2 = []
        numPivots = 0
        for num in nums:
            if num == pivot:
                numPivots += 1
            elif num < pivot:
                arr1.append(num)
            else:
                arr2.append(num)
        
        finalArr = arr1 + [pivot] *numPivots + arr2
        return finalArr