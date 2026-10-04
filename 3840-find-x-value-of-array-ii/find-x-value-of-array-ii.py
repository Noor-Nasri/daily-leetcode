# So hard to dicypher this question. brother. okay lets see..
# We start with nums. Each query updates a number, THEN asks a question:
# "Starting at ind, how many subarrays have (product % k) == x?"

# Seems complex, but k <= 5, and we only care for x < k. 
# We need some way to precompute the valid subarrays as we go.. We cant afford n^2.
# Can we somehow figure out the number of subarrays for each remainder first, then update as we go?
# Can start with DP: (ind, curRemainder, targetRemainder) -> either end the subarray or keep it going. 
# Okay, we can do a DP solution for the initial subarray counts, per remainder and per starting ind.
# But how do we update this per query?? There is a trick I am missing.

# Is it possible to do some tree structure, ie each node is a leaf, and update is O(log(n))?
# Then each node needs to hold facts about itself based on its children's facts, and we can update.
# We need to solve: [r0, r1, r2, r3, r4], ie # of subarrays with those remainders.
# To solve, each node needs to know these counts for the subarrays at the edges!
# Then updating a node is: Add left + right counts, and consider overlaps with at most 25 computations!

# Okay, that should work. Very complex.
# To update, just mult remainders and modulo again. Ex: k=3. Prod1 = 79, prod2 = 80. Remainders 1, 2 -> remainder 2 

# GAH: I implemented the main structure then realized that we need a way to pass in startInd
# We'd need to add some query method through the tree, to work up the answer from only the init value.
# Tricky byt still doable ..
    
class remainderNode:
    def __init__(self, nums, k, indLeft, indRight):
        if indLeft == indRight:
            self.arrayRemainder = nums[indLeft] % k
            remaindersTotal = [0 for i in range(k)] # I was tracking this but I realize we dont need it lol
            remaindersTotal[self.arrayRemainder] = 1
            
            self.remaindersLeft = remaindersTotal[::]
            self.remaindersRight = remaindersTotal[::]
            self.isLeaf = True
        else:
            self.isLeaf = False
            self.cutoff = (indLeft + indRight) // 2
            self.childLeft = remainderNode(nums, k, indLeft, self.cutoff)
            self.childRight = remainderNode(nums, k, self.cutoff + 1, indRight)
            self.updateRemainders(k)
    
    def updateRemainders(self, k):
        # Children values are valid, but ours need to be recomputed
        remainderLeft = self.childLeft.arrayRemainder
        remainderRight = self.childRight.arrayRemainder
        self.arrayRemainder = (remainderLeft * remainderRight) % k
        
        self.remaindersLeft = self.childLeft.remaindersLeft[::]
        for remR in range(k):
            viableFromRight = self.childRight.remaindersLeft[remR]
            resultRem = (remainderLeft * remR) % k
            self.remaindersLeft[resultRem] += viableFromRight

        self.remaindersRight = self.childRight.remaindersLeft[::]
        for remL in range(k):
            viableFromLeft = self.childLeft.remaindersRight[remL]
            resultRem = (remL * remainderRight) % k
            self.remaindersRight[resultRem] += viableFromLeft

    
    def updateVal(self, k, targetInd, newVal):
        if self.isLeaf:
            self.arrayRemainder = newVal % k
            remaindersTotal = [0 for i in range(k)]
            remaindersTotal[self.arrayRemainder] = 1
            self.remaindersLeft = remaindersTotal[::]
            self.remaindersRight = remaindersTotal[::]
            return
        
        if targetInd <= self.cutoff:
            self.childLeft.updateVal(k, targetInd, newVal)
        else:
            self.childRight.updateVal(k, targetInd, newVal)
        
        self.updateRemainders(k)
    
    def answerQuery(self, startingInd, targetRem, k):
        # Returns (# valid subarrays, remainder of [startingInd, indRight])
        if self.isLeaf:
            return (int(self.arrayRemainder == targetRem), self.arrayRemainder)
        elif startingInd > self.cutoff:
            return self.childRight.answerQuery(startingInd, targetRem, k)

        validArrays, remainderLeft = self.childLeft.answerQuery(startingInd, targetRem, k)
        for remR in range(k):
            viableFromRight = self.childRight.remaindersLeft[remR]
            resultRem = (remainderLeft * remR) % k
            if resultRem == targetRem:
                validArrays += viableFromRight
        
        return (validArrays, (remainderLeft*self.childRight.arrayRemainder) % k)
    

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        tree = remainderNode(nums, k, 0, len(nums) - 1)
        answers = []
        for targetInd, newVal, startingInd, targetRem in queries:
            tree.updateVal(k, targetInd, newVal)
            validArrays, _ = tree.answerQuery(startingInd, targetRem, k)
            answers.append(validArrays)
        
        return answers


        
        

