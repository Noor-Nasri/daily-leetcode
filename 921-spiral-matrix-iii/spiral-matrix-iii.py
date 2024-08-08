class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        results = [[rStart, cStart]]
        directions = [
            [0, 1], # Start RIGHT, then down, then left, then up, repeat
            [1, 0],
            [0, -1],
            [-1, 0]
        ]
        
        def stepOne(pos, dir):
            pos[0] += directions[dir][0] 
            pos[1] += directions[dir][1] 
            if 0 <= pos[0] < rows and 0 <= pos[1] < cols:
                results.append(pos[:])
            return pos

        def runSpiral(pos, dir, length):
            # pos included, now dir is updated and we run it
            for i in range(length):
                pos = stepOne(pos, dir)
            dir = (dir + 1) % 4
            for i in range(length):
                pos = stepOne(pos, dir)
            return [pos, (dir + 1) % 4]
        
        len_spiral = 1
        cur_dir = 0
        cur_pos = results[0][:]
        while len(results) < rows * cols:
            cur_pos, cur_dir = runSpiral(cur_pos, cur_dir, len_spiral)
            len_spiral += 1
        
        return results
                
            
        