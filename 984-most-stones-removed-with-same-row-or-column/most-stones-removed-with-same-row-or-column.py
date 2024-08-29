class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rowMappings = {} # [Row] -> group Ind
        colMappings = {}
        groups = []

        for col, row in stones:
            if not row in rowMappings and not col in colMappings:
                # New group
                groups.append([(row, col)])
                rowMappings[row] = len(groups) - 1
                colMappings[col] = len(groups) - 1
            
            elif row in rowMappings and not col in colMappings:
                # Add this col to the existing row 
                groups[rowMappings[row]].append((row, col))
                colMappings[col] = rowMappings[row]
            
            elif not row in rowMappings and col in colMappings:
                # Add this row to the existing col 
                groups[colMappings[col]].append((row, col))
                rowMappings[row] = colMappings[col]

            elif rowMappings[row] == colMappings[col]:
                groups[colMappings[col]].append((row, col))

            else:
                # Conflict, merge groups
                old_group_ind = rowMappings[row]
                new_group_ind = colMappings[col]

                groups[new_group_ind].append((row, col))
                for r, c in groups[old_group_ind]:
                    groups[new_group_ind].append((r, c))
                    rowMappings[r] = new_group_ind
                    colMappings[c] = new_group_ind
                
                groups[old_group_ind] = []

        total = 0
        for group in groups:
            if not group: continue
            total += len(group) - 1
        
        return total



