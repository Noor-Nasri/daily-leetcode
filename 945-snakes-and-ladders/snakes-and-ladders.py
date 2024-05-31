class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        maxTile = n**2
        options = [1]
        seen = set(options)
        dist = 1

        while options:
            #print(options)
            next_round = []
            for option in options:
                for move in range(1, 7):
                    target = option + move
                    if (target > maxTile): break

                    row = (target - 1) // n
                    extra = (target - 1) % n
                    #print(target, "means", row, extra)
                    
                    if row % 2 == 1:
                        jump = board[n - 1 - row][n - 1 - extra]
                    else:
                        jump = board[n - 1 - row][extra]
                    
                    if jump > -1:
                        #seen.add(target)
                        target = jump
                        
                    
                    #print("From", option, move, "can go to", target)
                    if (target in seen):
                        #print("Dupe, ignored") 
                        continue

                    if target == maxTile:
                        return dist

                    seen.add(target)
                    next_round.append(target)
                    



            options = next_round
            dist += 1



        return -1
        