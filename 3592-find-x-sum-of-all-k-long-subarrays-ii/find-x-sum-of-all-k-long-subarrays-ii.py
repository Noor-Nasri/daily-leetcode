from heapq import heappush, heappop

class Solution:
    # The obvious idea here would be something related to sliding window. 
    # We need to maintain the current occurances, as well as the subset for the top x elements and the sum.
    # How about 2 heaps, with the ability to update prio of existing elements?
    # Then we can maintain the frequencies inside the top x and outside the top x seperately. 
    # When the highest freq outside > lowest freq inside, we swap. and update variables

    def ensureMinFreqInXAboveMaxOutsideX(self):
        # Remove elements flagged for removal, then check if we need to swap the two elements
        #print("Adjusting", self.topXFreqMinHeap, self.remElementsMaxHeap)
        while self.topXFreqMinHeap and not self.topXFreqMinHeap[0][-1]:
            heappop(self.topXFreqMinHeap)
        
        while self.remElementsMaxHeap and not self.remElementsMaxHeap[0][-1]:
            heappop(self.remElementsMaxHeap)
        
        #print("Init pops yield", self.topXFreqMinHeap, self.remElementsMaxHeap)
        if not self.remElementsMaxHeap:
            #print("Nothing to move over")
            return
        
        if self.numInTopX < self.x:
            #print("Going to fill in the gaps")
            negFreq, negVal, isAlive = heappop(self.remElementsMaxHeap)
            newElement = [-negFreq, -negVal, True]
            self.numDB[-negVal] = [newElement, True] # ptr, isTopX
            self.curTotal += newElement[0]*newElement[1]
            heappush(self.topXFreqMinHeap, newElement)
            self.numInTopX += 1
            #print("New state:", self.topXFreqMinHeap, self.remElementsMaxHeap)
            return
        
        if self.topXFreqMinHeap[0][0] > -self.remElementsMaxHeap[0][0]:
            return
        elif self.topXFreqMinHeap[0][0] == -self.remElementsMaxHeap[0][0] and self.topXFreqMinHeap[0][1] > -self.remElementsMaxHeap[0][1]:
            return
        
        #print("Swapping!")
        freqFromOldTopX, valFromOldTopX, _= heappop(self.topXFreqMinHeap)
        negFreqFromOldRem, negValFromOldRem, _ = heappop(self.remElementsMaxHeap)
        newTopElement = [-negFreqFromOldRem, -negValFromOldRem, True]
        newRemElement = [-freqFromOldTopX, -valFromOldTopX, True]

        heappush(self.remElementsMaxHeap, newRemElement)
        heappush(self.topXFreqMinHeap, newTopElement)
        self.numDB[newTopElement[1]] = [newTopElement, True]
        self.numDB[-newRemElement[1]] = [newRemElement, False]

        self.curTotal += newTopElement[0]*newTopElement[1] - newRemElement[0]*newRemElement[1]
        #print("New state:", self.topXFreqMinHeap, self.remElementsMaxHeap)
        

    def adjustKnownValFreq(self, val, adj):
        #print("Adjusting existing element", val, "by", adj)
        heapElementPtr, isTopX = self.numDB[val]
        heapElementPtr[2] = False
        if isTopX:
            self.curTotal += val * adj
            newElement = [heapElementPtr[0] + adj, heapElementPtr[1], True]
            curHeap = self.topXFreqMinHeap
        else:
            newElement = [heapElementPtr[0] - adj, heapElementPtr[1], True]
            curHeap = self.remElementsMaxHeap
        
        if newElement[0]: # As long as its not 0, we should add the correct freq back into arr
            heappush(curHeap, newElement)
            self.numDB[val] = [newElement, isTopX]
        else:
            self.numDB[val] = None
            if isTopX:
                self.numInTopX -= 1


    def addValIntoWindow(self, val):
        if val in self.numDB and self.numDB[val] != None:
            self.adjustKnownValFreq(val, 1)
        else:
            #print("Adding new element")
            newElement = [-1, -val, True]
            self.numDB[val] = [newElement, False]
            heappush(self.remElementsMaxHeap, newElement)
    
    
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        self.topXFreqMinHeap = [] # [Freq, Val, isActive]
        self.remElementsMaxHeap = [] # [-Freq, -Val, isActive]
        self.numDB = {} # val -> [heapElementPtr, isTopX]
        self.x = x
        self.numInTopX = 0

        self.curTotal = 0
        for i in range(k):
            self.addValIntoWindow(nums[i])
            self.ensureMinFreqInXAboveMaxOutsideX()

        #print("Starting state:", self.curTotal, self.topXFreqMinHeap, self.remElementsMaxHeap)
        results = [self.curTotal]
        for i in range(k, len(nums)):
            self.adjustKnownValFreq(nums[i - k], -1)
            self.ensureMinFreqInXAboveMaxOutsideX()
            self.addValIntoWindow(nums[i])
            self.ensureMinFreqInXAboveMaxOutsideX()
            results.append(self.curTotal)
            #print("After looking at", nums[i], ":", self.curTotal, self.topXFreqMinHeap, self.remElementsMaxHeap)

        return results
