class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        remaining = [i for i in range(n)]
        cur_ind = 0
        k -= 1

        for i in range(n - 1):
            cur_ind = (cur_ind + k)%len(remaining)
            #print("Removing: ", remaining[cur_ind])
            del remaining[cur_ind]
            
            if cur_ind == len(remaining):
                cur_ind = 0
            
           # print("Current index is now", cur_ind)
        
        return remaining[0] + 1

        