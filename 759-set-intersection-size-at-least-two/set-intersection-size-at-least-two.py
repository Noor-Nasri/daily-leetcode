class Solution:
    # Suppose you look at the interval that ends first. Two days will have to be taken anyways, so just take the last 2. 
    # Since it ends earliest, we get as much overlap as possible. Soooo is that all?
    # Earliest end at 3: Take [2, 3]. Next earliest end: do we take 2, 1, or 0 numbers? Ie 0->5 or 4->5. 
    # We can just do n^2 to solve and move on. Feels like medium.

    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x : x[1])
        takenNumbers = set()

        for st, ed in intervals:
            numValsNeeded = 2
            for numTaken in takenNumbers:
                if st <= numTaken <= ed:
                    numValsNeeded -= 1
                    if numValsNeeded == 0:
                        break
            
            for newNum in range(ed, st - 1, -1):
                if not numValsNeeded:
                    break
                
                if newNum not in takenNumbers:
                    takenNumbers.add(newNum)
                    numValsNeeded -= 1
        
        return len(takenNumbers)
