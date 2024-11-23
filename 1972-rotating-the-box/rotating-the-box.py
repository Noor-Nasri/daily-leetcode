class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        shifted = [
            [box[old_row][old_col] for old_row in range(len(box))][::-1] 
            for old_col in range(len(box[0]))
        ]
        
        # Now for each column: push down all elements till obstacles, then continue moving
        for col in range(len(shifted[0])):
            curRow = 0
            chainLen = 0

            while curRow < len(shifted):
                if shifted[curRow][col] == "#":
                    chainLen += 1
                    shifted[curRow][col] = "."
                elif shifted[curRow][col] == "*":
                    # paste the chain above us
                    for above in range(chainLen):
                        shifted[curRow - 1 - above][col] = "#"
                    chainLen = 0
                curRow += 1
            
            for above in range(chainLen):
                shifted[len(shifted) - 1 - above][col] = "#"

        return shifted