# For each placement, we would want to scan all obstacles to find a gap>=sx before x.
# obv that would TLE, so we need to either organize the obstacles in a funny tree, or build backwards

# Tree approach means somehow maintaining largestGapUntil for every obstacle, then finding last obstacle
# Building backwards means the placement comes first and just put at 0, but shifted as we keep going
# Tree might be easier if we scope it out properly .. is there any other idea? x is iterable ..

# I went and learned about segment trees, very cool!
# Essentially the root node represents the full [0, n] range, then any insert is pre-defined.
# Ie [0, 10] then inserting 2 means [0, 10] splits to [0, 4], [5, 10] then [0, 4] splits to [0, 2], [3, 4]
# Then [0, 2] splits down to [0, 1] and [2] which actually holds our value! Then we update any properties upwards
# So segment trees are essentially BSTs that operate on a limited range, allowing us to predefine a balanced path for all nodes

# So the plan is: Prefill 1->n (up to 5*10^4 leaf nodes and another 5*10^4 range nodes). 
# Then track smallest val, biggest val, and max gap in every range node. maxGap = max(maxLeft, maxRight, smallestRight - biggestLeft)
# Then placement query goes down to leaf node, and solve maxGapTillX = max(maxLeft, maxRightUntilX, min(smallestRight, x) - biggestLeft)
    
class SegmentNode:
    def __init__(self, minVal, maxVal):
        #print("Creating Node", minVal, maxVal)
        self.intervalMin = minVal
        self.intervalMax = maxVal
        self.maxGap = maxVal - minVal
        self.actualMin = 0
        self.actualMax = 0

        if minVal == maxVal:
            self.isLeaf = True
            self.active = False # don't really need this, but it makes it easier to follow
        else:
            self.splitVal = (minVal + maxVal) // 2
            self.leftNode = SegmentNode(minVal, self.splitVal)
            self.rightNode = SegmentNode(self.splitVal + 1, maxVal)
            self.isLeaf = False
    
    def enableObstacle(self, x):
        # Goes down to deepest node, and updates the whole chain down with new values
        if self.isLeaf:
            self.active = True
            return
        elif x <= self.splitVal:
            self.leftNode.enableObstacle(x)
        else:
            self.rightNode.enableObstacle(x)

        self.actualMin = min(self.actualMin or x, x)
        self.actualMax = max(self.actualMax, x)
        maxGapAcross = (self.rightNode.actualMin or self.intervalMax) - (self.leftNode.actualMax or self.intervalMin)
        self.maxGap = max(self.leftNode.maxGap, self.rightNode.maxGap, maxGapAcross)
        #print("Enabling node", self.intervalMin, self.intervalMax, "for value", x, f"which creates actualMin={self.actualMin}, actualMax={self.actualMax}, maxGap={self.maxGap}")

    def solveMaxGapUntilX(self, x):
        if self.isLeaf:
            return 0
        elif x <= self.splitVal:
            gap = self.leftNode.solveMaxGapUntilX(x)
            #print("Searching node", self.intervalMin, self.intervalMax, "for limit", x, f"which means gap = leftGapUntilX={gap}")
            return gap
        
        maxRightGapUntilX = self.rightNode.solveMaxGapUntilX(x)
        maxGapAcrossUntilX = min((self.rightNode.actualMin or self.intervalMax), x) - (self.leftNode.actualMax or self.intervalMin)
        #print("Searching node", self.intervalMin, self.intervalMax, "for limit", x, f"which means leftGap={self.leftNode.maxGap} maxRightGapUntilX={maxRightGapUntilX}, maxGapAcrossUntilX={maxGapAcrossUntilX}")
        return max(self.leftNode.maxGap, maxRightGapUntilX, maxGapAcrossUntilX)
        
        

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        maxPos = max(e[1] for e in queries)
        segmentTree = SegmentNode(0, maxPos)
        answers = []

        for query in queries:
            #print("=======")
            if query[0] == 1:
                #print("Enabling obs", query[1])
                segmentTree.enableObstacle(query[1])
                continue
                
            _, x, sz = query
            if segmentTree.actualMax + sz <= x:
                # We dont need to go into the tree, this can be placed beyond all obstacles
                answers.append(True)
            else:
                #print("Searching for value limit at", x)
                maxGap = segmentTree.solveMaxGapUntilX(x)
                answers.append(maxGap >= sz)

        return answers




