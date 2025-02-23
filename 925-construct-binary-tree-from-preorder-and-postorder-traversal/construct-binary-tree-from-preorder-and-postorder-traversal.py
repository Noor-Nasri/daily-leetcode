# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def makeNode(self, value, curStack, postOrdering):
        # If value is child of our deepest level, it will appear BEFORE the parent in post ordering
        # this is because ALL descendants will print before parents. 
        # And the preorder ensures that that all future nodes will be descendants of this one, or to the right
        # So if the new node comes after the top of our stack, the top of our stack will not get any more descendants. So it can be ignored.
        newNode = TreeNode(value)
        if not curStack:
            curStack.append(newNode)
            return
        
        parentNode = curStack[-1]
        while not (postOrdering[newNode.val] < postOrdering[parentNode.val]):
            curStack.pop() 
            parentNode = curStack[-1]

        if parentNode.left == None:
            parentNode.left = newNode
        else:
            parentNode.right = newNode
        
        curStack.append(newNode)


    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postOrdering = {}
        for ind in range(len(postorder)):
            postOrdering[postorder[ind]] = ind

        curStack = []
        for value in preorder:
            self.makeNode(value, curStack, postOrdering)
        
        return curStack[0]

        