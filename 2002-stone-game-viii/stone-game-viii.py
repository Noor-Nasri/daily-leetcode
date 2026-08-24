class Solution:
    # Alice can always secure the total sum and end the game immediately. 
    # Okay I was thinking alice just forces n or n-1 from the start, BUT:
    # There is a trick with negatives.  Imagine sum(...) = 70, -64
    # Alice takes 70, Bob is forced to take only 6, then Alice can take the 6. Diff=70. 

    # DP[curInd] = optimal selection (sumUntilInd, curInd, ...)
    # How do we do that loop without n^2 total? Can we do BS wiithin the DP loop?
    # How can we reduce the DP into 2 options instead of n without moving n to input?
    # Can we somehow pack (prevChosen, curLength) into nlogn?
    # Okay i peeked the hint and it says to just do the n^2? Am i crazy?
    # Whats the optimization here .. there is some way to avoid a full loop.
    
    # Can't we just track the worst ind so far (backwards), and always use that?
    # SO: suppose ind=5 checks everything, and determines taking [sum0->5, 6, 7, 8] is optimal
    # Where this gives maxScoreDiff=10.
    # Now when you go to ind=4, checking against all those inds only changes all the values by vals[4]
    # So then we know [sum0->4, 5, 6, 7, 8] is STILL optimal! 
    # The only other idea to consider is the one we didnt check before: [sum0->4, 5]

    # So now DP is only TWO options: Take 2 elements, OR take until known best!
    # This took me way too long to think about ... I need to practice and sleep man.

    def stoneGameVIII(self, stones: List[int]) -> int:
        prefixSums = stones[:]
        for ind in range(1, len(prefixSums)):
            prefixSums[ind] += prefixSums[ind - 1]

        maxScoreDiffAtInd = [0 for i in range(len(stones))]
        bestScoreSoFar = prefixSums[-1]
        maxScoreDiffAtInd[-2] = bestScoreSoFar

        for ind in range(len(stones) - 3, -1, -1):
            #bestScoreSoFar += stones[ind] # All scores in last ind carry over, with an extra val
            option2 = prefixSums[ind + 1] - maxScoreDiffAtInd[ind + 1] # Take just those 2 nums
            #print("Looking at ind", ind, "we can go until best ind for diff=", bestScoreSoFar, "or just take n=2 for diff=", option2)
            bestScoreSoFar = max(bestScoreSoFar, option2)
            maxScoreDiffAtInd[ind] = bestScoreSoFar

        #print("Original:   ", stones)
        #print("Sums:       ", prefixSums)
        #print("Max scores: ", maxScoreDiffAtInd)
        return maxScoreDiffAtInd[0]


        