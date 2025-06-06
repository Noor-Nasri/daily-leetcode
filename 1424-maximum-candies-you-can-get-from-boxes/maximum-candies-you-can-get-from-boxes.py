class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        total = 0
        isOpen = status[:]
        canVisitOnceOpened = set()
        readyOptions = [] 
        visited = set()

        for box in initialBoxes:
            if isOpen[box]:
                readyOptions.append(box)
                visited.add(box)
            else:
                canVisitOnceOpened.add(box)

        while readyOptions:
            box = readyOptions.pop()
            total += candies[box]

            for newBox in containedBoxes[box]:
                if newBox in visited: continue
                if isOpen[newBox]:
                    readyOptions.append(newBox)
                    visited.add(newBox)
                else:
                    canVisitOnceOpened.add(newBox)

            for key in keys[box]:
                isOpen[key] = 1
                if key in canVisitOnceOpened:
                    canVisitOnceOpened.remove(key)
                    readyOptions.append(key)
                    visited.add(key)

        return total