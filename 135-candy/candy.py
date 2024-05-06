class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = len(ratings) # start at 1 per person, increase as required
        n = len(ratings)
        ind = 1
        last_value = 1 # number of candies given at [ind - 1]

        while (ind < n):
            if (ratings[ind] < ratings[ind - 1]): 
                # MUST be smaller than prev, first see how far the chain goes
                chain_end = ind + 1
                while (chain_end < n):
                    if (ratings[chain_end] < ratings[chain_end - 1]):
                        chain_end += 1
                    else:
                        break

                # This means, this chain takes form [... 3 2 1]
                # Total extra candy, excluding ind-1, is .. + 2 + 1
                sequence_length = chain_end - ind - 1
                candy += sequence_length * (1 + sequence_length) / 2
                                
                # Finally, resolve that ind must be smaller than ind-1
                # That means, ind-1 must be bigger than ind
                if (last_value <= sequence_length + 1):
                    candy += sequence_length + 2 - last_value

                ind = chain_end
                last_value = 1
            else:
                if (ratings[ind] > ratings[ind - 1]):
                    # MUST give another X candy to this one
                    candy += last_value
                    last_value+=1
                else:
                    last_value=1
                ind += 1 

        return int(candy)


        