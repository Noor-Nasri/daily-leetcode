class graphNode:
    def __init__(self, val):
        self.val = val
        self.parents = set()
        self.children = []
        self.inserted = False

class Solution:
    def includeNode(self, ordering, nodes, val):
        node = nodes[val]
        if node.parents or node.inserted:
            return # cant include
        
        ordering.append(val)
        node.inserted = True
        #print("Added", val)
        
        for child in node.children:
            #print("Removing constraint", val, "from", child)
            child_node = nodes[child]
            if val in child_node.parents:
                child_node.parents.remove(val)

        for child in node.children:
            self.includeNode(ordering, nodes, child)


    def solveOrdering(self, k, conditions):
        nodes = [graphNode(i) for i in range(k + 1)] #ignore ind 0
        for before, after in conditions:
            nodes[after].parents.add(before)
            nodes[before].children.append(after)
    
        ordering = []
        for i in range(1, k + 1):
            self.includeNode(ordering, nodes, i)
        
        return ordering


    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        #print("Rows")
        row_orders = self.solveOrdering(k, rowConditions)
        #print("Cols")
        col_orders = self.solveOrdering(k, colConditions)
        
        if len(row_orders) != k or len(col_orders) != k: 
            return []

        result = [[0 for i in range(k)] for j in range(k)]
        indices = [[-1, -1] for i in range(k + 1)]
        for ind in range(k):
            value_at_row_ind = row_orders[ind]
            value_at_col_ind = col_orders[ind]

            indices[value_at_row_ind][0] = ind
            indices[value_at_col_ind][1] = ind

        for val in range(1, k + 1):
            row, col = indices[val]
            result[row][col] = val
        
        return result
