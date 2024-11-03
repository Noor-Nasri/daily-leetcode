class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set(tuple(e) for e in obstacles)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # go forward with -1, back with -2
        pos = [0,0]
        dir_ind = 0
        max_dist = 0

        for command in commands:
            if command < 0:
                dir_dir = command == -1 and 1 or -1
                dir_ind = (dir_ind + dir_dir) % 4
                continue
            
            for move in range(command):
                next_x = pos[0] + directions[dir_ind][0]
                next_y = pos[1] + directions[dir_ind][1]
                if (next_x, next_y) in obstacles:
                    break
                
                pos = [next_x, next_y]


            max_dist = max(max_dist, pos[0]**2 + pos[1]**2)
        return max_dist

        