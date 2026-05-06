class Solution:
    # We need to go through each row to create the corresponding flipped column
    # The trick is to loop through the row backwards and maintain the ptr for the fall result
    # We can think of this as shifting all the way right, then putting it on the flipped grid

    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        nRowOrig, nColOrig = len(boxGrid), len(boxGrid[0])
        newGrid = [["." for col in range(nRowOrig)] for row in range(nColOrig)]    

        for origRow in range(nRowOrig):
            newCol = nRowOrig - 1 - origRow
            nextAvailPos = nColOrig - 1
            for origCol in range(nColOrig - 1, -1, -1):
                value = boxGrid[origRow][origCol]
                if value == "*":
                    newGrid[origCol][newCol] = "*"
                    nextAvailPos = origCol - 1
                elif value == "#":
                    # Imagine # shifts all the way right to nextAvailPos
                    # Then we flip (row, col) -> (col, nrow - row)
                    newGrid[nextAvailPos][newCol] = "#"
                    nextAvailPos -= 1
        
        return newGrid