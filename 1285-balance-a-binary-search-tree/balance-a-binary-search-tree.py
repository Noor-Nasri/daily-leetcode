# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # So we just get all the values then make a new tree thats balanced.
    # If all the values are sorted: middle element is root, then balance based on the two subtrees
    # Since its given as BST, we can get sorted then create in O(N)

    def fillSortedArr(self, root):
        if root == None:
            return
        self.fillSortedArr(root.left)
        self.sortedArr.append(root.val)
        self.fillSortedArr(root.right)
    
    def createBalancedTree(self, startInd, endInd):
        midInd = (startInd + endInd) // 2
        rootNode = TreeNode(self.sortedArr[midInd])
        if startInd < midInd:
            rootNode.left = self.createBalancedTree(startInd, midInd - 1)
        
        if endInd > midInd:
            rootNode.right = self.createBalancedTree(midInd + 1, endInd)
        
        return rootNode

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sortedArr = []
        self.fillSortedArr(root)
        return self.createBalancedTree(0, len(self.sortedArr) - 1)