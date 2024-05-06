class Solution:
    def candy(self, ratings: List[int]) -> int:
        assignments = [1 for i in range(len(ratings))]
        ind = 1
        n = len(ratings)


        while (ind < n):
            if (ratings[ind] < ratings[ind - 1]): 
                # Must be smaller than prev, first see how far the chain goes
                chain_end = ind + 1
                while (chain_end < n):
                    if (ratings[chain_end] < ratings[chain_end - 1]):
                        chain_end += 1
                    else:
                        break

                # Now go backwards to set them
                # This is still O(n) overall because chains dont overlap
                if chain_end - ind > 1:
                    for backward_ind in range(chain_end - 2, ind - 1, -1):
                        assignments[backward_ind] = assignments[backward_ind + 1] + 1
                
                # Finally, resolve that ind must be smaller than ind-1
                assignments[ind - 1] = max(assignments[ind - 1], assignments[ind] + 1)
                ind = chain_end
            else:
                # Check if we need to increase, otherwise keep at 1 and go next
                if (ratings[ind] > ratings[ind - 1] and assignments[ind] <= assignments[ind - 1]):
                    assignments[ind] = assignments[ind - 1] + 1 
                    
                ind += 1 
        return sum(assignments)


        