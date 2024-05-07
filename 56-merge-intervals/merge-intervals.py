class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        values = [0 for i in range(10001)]
        singles = set()

        for interval in intervals:
            if interval[0] == interval[1]:
                # edge case
                singles.add(interval[0])
            else:
                values[interval[0]] += 1
                values[interval[1]] -= 1
        
        merged = []
        cur_sum = 0
        cur_start = -1
        for ind in range(len(values)):
            cur_sum += values[ind]
            if (cur_sum > 0 and cur_start == -1):
                # Started a new interval
                cur_start = ind
            elif (cur_sum == 0 and cur_start > -1):
                # Finished an old interval
                merged.append([cur_start, ind])
                cur_start = -1
            elif (cur_sum == 0 and ind in singles):
                # Must include (inc, inc) since it was provided
                merged.append([ind, ind])

        return merged

