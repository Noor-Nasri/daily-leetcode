class Solution:
    # First instinct is binary search, but its not clear how we can verify if the energy is sufficient
    # The same # of energy will work/fail based on the ordering of tasks, but if we solve that we may not even need BS
    # Even if we wanted to mimic the choices with DP, it becomes (completed) -> try any remaining. So best case is n^2.
    # The core of this question has to be some tricky greedy to figure out the ideal task order, at least for an init energy.

    # If we have enough energy, is it okay to just always take whichever job allows you to have most remaining?
    # Eg: Required 10 and cost 3 means we have >= 7 at the end, so we do it before [5, 6] which has >= 1. 
    
    # If we do this, can we ever get to remaining < required -> fail while another order would have worked?
    # I think no, because if we took this job earliest, we still need to have enough energy for the ones with higher entryPoints
    # I cant think of a counter example so we'll just try it
    
    def attemptTasks(self, tasks, energy):
        for cost, req in tasks:
            if energy < req:
                return False
            
            energy -= cost
        return True

    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks = sorted(tasks, key = lambda x : x[1] - x[0], reverse = True)
        low = 0
        high = 10**9
        best = -1

        while low <= high:
            mid = (low + high) // 2
            if self.attemptTasks(tasks, mid):
                best = mid
                high = mid - 1
            else:
                low = mid + 1

        
        return best