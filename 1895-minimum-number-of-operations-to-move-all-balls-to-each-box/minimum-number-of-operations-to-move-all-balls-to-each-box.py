class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        solution = []
        for desired_box in range(len(boxes)):
            numMoves = 0
            for other_box in range(len(boxes)):
                if desired_box == other_box or boxes[other_box] == '0':
                    continue
                
                numMoves += abs(desired_box - other_box)


            solution.append(numMoves)

        return solution
        