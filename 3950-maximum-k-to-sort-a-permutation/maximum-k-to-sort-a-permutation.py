class Solution:
    # This feels like a trick question. How can this be guaranteed to work?
    # Imagine you pick value 0: Now 0 can be swapped with any number. Just use it to move everything!
    # Value 1: Now 1 can be swapped with 1, 3, 5, 7, 9, ... Even values cant move
    # Value 3: 1 and evens cant move. But 3 can move across 7, 11, .. (Jump by + 4)
    # So odd values can be solved, sweep or BS. However evens are more challenging.

    # Value 2: 2 can swap with 6, 10, 14. ALSO with 3, 7, 11, 15
    # Value 4: 4,5,6,7 all swapable and then expand + 8s. 12,13,14,15, ...
    # So choosing 2 means you adjust 2,3, 6, 7, 10, 11, 14, 15
    # While doing 4 means you adjust 4,5,6,7, 12,13,14,15

    # I think we just figure out what vals are out of place, and work out some combined AND. 

    def sortPermutation(self, nums: List[int]) -> int:
        totalANDOfElementsOutOfPlace = 2**17 - 1
        isSorted = True
        for i in range(len(nums)):
            if nums[i] != i:
                totalANDOfElementsOutOfPlace &= i
                isSorted = False
        
        if isSorted:
            return 0
            
        return totalANDOfElementsOutOfPlace
        