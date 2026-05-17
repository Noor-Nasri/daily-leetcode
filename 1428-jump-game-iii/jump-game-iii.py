class Solution:
    # Seems like a pretty standard search, just explore and ignore seen
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = {start}
        explore = [start]
        while explore:
            ind = explore.pop()
            val = arr[ind]
            if val == 0:
                return True
            
            for newInd in [ind - val, ind + val]:
                if (0 <= newInd < len(arr)) and newInd not in seen:
                    seen.add(newInd)
                    explore.append(newInd)
            
            
        return False
        