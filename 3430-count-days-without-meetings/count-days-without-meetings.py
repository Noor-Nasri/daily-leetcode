class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings, key = lambda x : x[0])
        
        counter = max(meetings[0][0] - 1, 0)
        #print("Starting", counter)
        
        curEnd = meetings[0][1]
        
        for i in range(1, len(meetings)):
            start, end = meetings[i]
            
            if start > days: break # No need to count extra
            
            if start <= curEnd: # No gap
                curEnd = max(curEnd, end)
            else:
                #print("Adding gap", curEnd, start)
                counter += start - curEnd - 1
                curEnd = end
                
                if (curEnd >= days): break
        
        if curEnd < days:
            #print("Finishing gap", days, curEnd)
            counter += days - curEnd
        
        #print("Final", counter)
        return counter
                
    
        