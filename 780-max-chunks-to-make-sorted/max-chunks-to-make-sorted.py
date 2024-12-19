class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # Each number tells us where it must be, so we have that minimum length to sort
        # Since a number cant be in two chunks, any overlap causes a merge
        requiredSorts = []
        
        for ind in range(len(arr)):
            vals = [ind, arr[ind]]
            requiredSorts.append((min(vals), max(vals)))

        requiredSorts = sorted(requiredSorts)
        numChunks = 0
        curChunkEnd = -1
        for s, e in requiredSorts:
            if s > curChunkEnd:
                numChunks += 1
                curChunkEnd = e
            else:
                curChunkEnd = max(curChunkEnd, e)

        return numChunks
