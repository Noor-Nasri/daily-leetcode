class Solution:
    def findCutoff(self, n1, n2, allowedSum):
        # returns number of numbers we can include
        low = 0
        high = n2 - n1
        lastValid = 0

        while low <= high:
            mid = (low + high) // 2
            num_sum = (2 * n1 + mid - 1)/2 * mid
            if num_sum > allowedSum:
                high = mid - 1
            else:
                lastValid = mid
                low = mid + 1
        
        return lastValid

    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned.append(0)
        banned.append(n + 1)
        banned = sorted(banned)
        num_nums = 0
        total = 0

        for ind in range(len(banned) - 1):
            cur_banned = banned[ind]
            next_banned = banned[ind + 1]
            if cur_banned > n: 
                break

            if next_banned <= cur_banned + 1:
                continue
            
            sum_gap = (cur_banned + next_banned)/2 * (next_banned - cur_banned - 1)
            if total + sum_gap == maxSum:
                return num_nums + next_banned - cur_banned - 1
            elif total + sum_gap < maxSum:
                total += sum_gap
                num_nums += next_banned - cur_banned - 1
            else:
                # cant include entire gap, find biggest number we can include
                num_extra =  self.findCutoff(cur_banned + 1, next_banned - 1, maxSum - total)
                return num_nums + num_extra
        
        return num_nums