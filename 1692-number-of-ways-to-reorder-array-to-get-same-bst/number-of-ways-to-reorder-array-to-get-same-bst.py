from math import comb
# So if we build the tree, then each node expands downwards:
# If [Left] has 5 ways to place 4 nodes and [Right] has 6 ways to place 5 nodes ..
# Then we have 9C4 * 5 * 6. Ie, pick which slots are for left and right, then multiply for the inner permutes.

# There is probably a way to optimize this to be O(n) by moving the choosing values up
# But I think this works anyways. Each node returns [Permute Count, Descendent Count], and does a fresh nCr
# So it's n^2 because nCr has an n! computation, and the whole tree takes n to iterate.

class Node:
    # Since we only want one final answer, we just add one last computation
    # If we needed multiple, we would store in self and update each add
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def add(self, val):
        chosenNode = self.left if val < self.val else self.right
        if chosenNode:
            chosenNode.add(val)
        elif val < self.val:
            self.left = Node(val)
        else:
            self.right = Node(val)
    
    def solvePermuteCounts(self, MOD):
        if self.left == None and self.right == None:
            return (1, 1) # 1 permute, 1 count
        elif self.left == None or self.right == None:
            # Only one child, we always come first then they have the permutes
            child = self.left or self.right
            numPermutes, numNodes = child.solvePermuteCounts(MOD)
            return (numPermutes, numNodes + 1)
        else:
            permutesLeft, countLeft = self.left.solvePermuteCounts(MOD)
            permutesRight, countRight = self.right.solvePermuteCounts(MOD)
            waysToMixChildren = comb(countLeft + countRight, countLeft) % MOD
            totalPermutes = (permutesLeft * permutesRight * waysToMixChildren) % MOD
           
            return (totalPermutes, countLeft + countRight + 1)


class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        root = Node(nums[0])
        for ind in range(1, len(nums)):
            root.add(nums[ind])
        
        totalPermutes, _ = root.solvePermuteCounts(10**9 + 7)
        return totalPermutes - 1
        