class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])

        merged = []
        cur = intervals[0]

        for i in range(1, len(intervals)):
            if (intervals[i][0] <= cur[1]):
                # Meeting started before last ended, extend
                if intervals[i][1] > cur[1]:
                    cur[1] = intervals[i][1]
            else:
                merged.append(cur)
                cur = intervals[i]
        
        merged.append(cur)
        return merged
