from collections import deque

class Solution:
    def canFinish(self, flower_days, day, m, k):
        done = 0
        ind = 0

        while (ind < len(flower_days)):
            if flower_days[ind] > day:
                ind+=1
                continue
            
            ind += k
            done += 1
            if done == m:
                return True

        return False

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay): return -1
        # This is a difficult medium, honestly should be hard. 
        # I first come up with two ideas, but they were both O(n^2)
        # Given the constraints, they would TLE or MLE

        # After looking at the hint, it occured to me that this can be done by
        # binary searching the planting day. ie log(10^9) = ~30
        # and a simple O(n) iteration at each point to check if possible

        # First, we need to assign bouqet_index -> min plant day
        # This can be made O(nlogn) with BSTs, but for now I'll ignore
        cur = deque(bloomDay[i] for i in range(k))
        flower_days = [max(cur)]
        for start in range(len(bloomDay) - k):
            cur_max = flower_days[-1]
            old_val = cur.popleft()
            new_val = bloomDay[start + k]
            cur.append(new_val)

            if (new_val > cur_max):
                flower_days.append(new_val)
            elif (old_val == cur_max): # max might be removed
                flower_days.append(max(cur))
            else: # old max still best
                flower_days.append(cur_max)
        
        
        low = min(flower_days)
        high = max(flower_days)

        while (low <= high):
            mid = (low + high) // 2

            if self.canFinish(flower_days, mid, m, k):
                if high == low: return mid
                high = mid
            else:
                low = mid + 1

        
        return -1 # wont happen, if statement catches all



        