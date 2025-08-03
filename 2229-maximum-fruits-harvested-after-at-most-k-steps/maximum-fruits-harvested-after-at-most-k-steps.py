class Solution:
    def exploreDir(self, posToFruit, initPos, k, majorDir):
        print("Exoloring dir", majorDir)
        total = 0
        rangeStart = initPos
        rangeEnd = initPos + k * majorDir
        for p in range(rangeStart, rangeEnd + majorDir, majorDir):
            total += posToFruit.get(p, 0)
        
        maxTotal = total
        for _ in range((k + 1)//2):
            # Instead of going all the way to end, we might go one more the other way first, so we end up two points behind the end.
            total -= posToFruit.get(rangeEnd, 0)
            rangeEnd -= majorDir
            total -= posToFruit.get(rangeEnd, 0)
            rangeEnd -= majorDir
            rangeStart -= majorDir
            total += posToFruit.get(rangeStart, 0)
            maxTotal = max(maxTotal, total)

        
        return maxTotal


    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # Slightly diff sliding window, since going one way means you have to 'undo' the path. 
        # You can go up to k units to the left, or instead go 2 less left for 1 more right. (ie go right then go left)
        # Likewise, you can first go left then go all the way right, so you start at +k and try 1 more left for 2 less right.
        # O(k) as we try every possible endpoint. Can do prefix sums or running sums.
        posToFruit = {}
        for p, f in fruits:
            posToFruit[p] = f
        
        op1 = self.exploreDir(posToFruit, startPos, k, 1)
        op2 = self.exploreDir(posToFruit, startPos, k, -1)
        return max(op1, op2)

        