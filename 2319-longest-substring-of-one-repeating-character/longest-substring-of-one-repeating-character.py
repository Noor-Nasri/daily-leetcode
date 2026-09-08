# We need some sort of segment tree that maintains the length of longest pattern
# When a node changes, it goes up all the way to reach root properly. 
# But the implementation of this seems complex. Only the direct chain would be correct updated.
# For example, nodes 0,1 and 2,3 are children to a0, a2 with granparent b0.
# If node 1, 2 are the same -> a0 and a2 are not aware of pattern but b0 is.
# If 2 is updated -> now b0 needs to know. But if it matches with 3, 4 -> now other side

# Question: if a chain of 10 gets broken but there was another chain of 9
# How do we recognize the 9 as the new max chain?
# Does each node need to maintain its own PQ of ranges? Too expensive!
# Instead: whatever node choose 10 over 9 in the past needs to fix it on the way up.

class Node:
    # Self managing nodes that maintains maxLen of repeating characters inside
    # The max is built based on children values, meaning updates go all the way down
    # Then fix all the way up.
    # Note: This is a segment tree, every node has 0 or 2 children.

    def updateLens(self):
        self.chainLenLeft = self.nodeLeft.chainLenLeft
        self.chainLenRight = self.nodeRight.chainLenRight
        maxAcross = 0

        if self.nodeLeft.charRight == self.nodeRight.charLeft:
            if self.chainLenLeft == self.nodeLeft.n:
                self.chainLenLeft += self.nodeRight.chainLenLeft
            
            if self.chainLenRight == self.nodeRight.n:
                self.chainLenRight += self.nodeLeft.chainLenRight
            
            maxAcross = self.nodeLeft.chainLenRight + self.nodeRight.chainLenLeft
        
        maxSplit = max(self.nodeLeft.maxLen, self.nodeRight.maxLen)
        self.maxLen = max(maxSplit, maxAcross)


    def __init__(self, s, rangeStart, rangeEnd):
        self.rangeStart, self.rangeEnd  = rangeStart, rangeEnd
        self.charLeft, self.charRight = s[rangeStart], s[rangeEnd]
        self.chainLenLeft, self.chainLenRight = 1, 1
        self.n = rangeEnd - rangeStart + 1
        self.isLeaf = False
        self.maxLen = 1

        if rangeStart == rangeEnd:
            self.isLeaf = True
        else: 
            self.cutoff = (rangeStart + rangeEnd) // 2
            self.nodeLeft = Node(s, rangeStart, self.cutoff)
            self.nodeRight = Node(s, self.cutoff + 1, rangeEnd)
            self.updateLens()

    def updateLeaf(self, ind, newChar):
        if self.isLeaf:
            self.charLeft, self.charRight = newChar, newChar
            return

        # Send down to proper children then recompute our lens
        if ind <= self.cutoff:
            self.nodeLeft.updateLeaf(ind, newChar)
        else:
            self.nodeRight.updateLeaf(ind, newChar)
        self.updateLens()

        # Our parent computation is based on our vals, so also update this
        if ind == self.rangeStart:
            self.charLeft = newChar
        elif ind == self.rangeEnd:
            self.charRight = newChar
        


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        rootNode = Node(s, 0, len(s) - 1)
        answers = []
        for queryInd in range(len(queryCharacters)):
            rootNode.updateLeaf(queryIndices[queryInd], queryCharacters[queryInd])
            answers.append(rootNode.maxLen)
        
        return answers
        