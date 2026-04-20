class Solution:
    # This is easy but we can optimize it like medium. 
    # The cool thing here is that the dist will always include the first or last house
    # For example, say max dist uses (i, j). If c[0] != c[j], then 0 is better than i.
    # Same thing: if c[-1] != c[i], then last element is better than j.
    # So now the only case without replacement is. [0] == [j], [-1] == i. So just use (0, -1)! 

    def maxDistance(self, colors: List[int]) -> int:
        maxDiff = 0
        for ind in range(len(colors) - 1, -1, -1):
            if colors[ind] != colors[0]:
                maxDiff = ind
                break
        
        for ind in range(len(colors)):
            if colors[ind] != colors[-1]:
                maxDiff = max(maxDiff, len(colors) - ind - 1)
                break

        return maxDiff