# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def treeQueries(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[int]
        """
        # pre-calculate height for each node: left subtree height and right subtree height
        levels = {}
        heights = {}
        self.calculateHeightDepth(root, 0, heights, levels)

        for key, val in levels.items():
            levels[key] = sorted(levels[key], key=lambda x: x[1], reverse=True)

        # print(heights)
        # print(depths)
        print(levels)
        
        answer = []
        for query in queries:
            ans = self.calculateQuery(query, heights, levels)
            answer.append(ans)
        return answer
    def calculateHeightDepth(self, node, cur_height, heights, levels):
        if not node:
            return -1
        
        heights[node.val] = cur_height
        
        
        left = self.calculateHeightDepth(node.left, cur_height + 1, heights, levels)
        right = self.calculateHeightDepth(node.right, cur_height + 1, heights, levels)
        depth = 1 + max(left, right)
        if levels.get(cur_height):
            levels[cur_height].append((node.val, depth))
        else:
            levels[cur_height] = [(node.val, depth)]
        return depth
    
    def calculateQuery(self, query, heights, levels):
        level = heights[query]
        same_level = levels[level]
        max_depth = 0
        for node, depth in same_level:
            if node != query:
                return  depth + level if len(same_level) > 1 else level - 1
        return level - 1