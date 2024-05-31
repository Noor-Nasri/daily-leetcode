class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0: return [newInterval]

        results = []
        cur = 0

        # Prev intervals: include all that end before we start
        while cur < len(intervals) and intervals[cur][1] < newInterval[0]: 
            results.append(intervals[cur]) 
            cur += 1
        
        if cur == len(intervals):
            results.append(newInterval)
            return results
        
        # Merge as necessary
        if intervals[cur][0] > newInterval[1]:
            # No overlap, just put in place
            results.append(newInterval)
        else:
            # Create one as necessary
            starting = min(newInterval[0], intervals[cur][0])
            ending = max(newInterval[1], intervals[cur][1])

            while (cur < len(intervals) and intervals[cur][0] <= ending):
                ending = max(ending, intervals[cur][1])
                cur += 1
            
            results.append([starting, ending])

        # Add remaining
        while cur < len(intervals): 
            results.append(intervals[cur]) 
            cur += 1

        return results
        