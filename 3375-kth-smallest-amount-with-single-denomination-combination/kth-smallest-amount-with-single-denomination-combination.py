class Solution:
    # This is an odd question. Constraints are super low except k is very big
    # So if they want the 10^9th smallest value, we will need some form of BS
    # Since only 15 coins, can we just do BS per coin? Start at coin1: low=1, high=k
    # At each mid, we consider all other coin values to find # combos < chosen
    # Then if we dont find a match, try again with coin2

    # Problem: How can we avoid double counting identical values?
    # For every (15 * logk occurs) verification:
    # --> Loop every number for # of multiples < chosen
    # ---> Then Loop across all numbers to exclude collisions
    # But then we can exclude a value multiple times! 

    # I think the trick lies in values <= 25. Can we do something cheeky..
    # Maybe just figure out how many valid multiples until LCM, scale it up, then solve the tail.
    # Issue: 1->25 LCM is 26 billion. So that doesnt work..
    # Can we do: given the chosen number, for each exclusion pair: 
    # get number of new values in [0, a*b]. Then scale it up. Still no, a*b->2*a*b doesnt have to be identical

    # Okay: new trick idea. We exclude, then we re-include the double exclusions, then re-exclude, etc.
    # EG: Vals: 2, 3, 7, 11. Pick value=11, count=6.
    # So now we compute col(2, 11, <66)= 22, 44 so 2.
    # Now compute col(3, 11, <66)
    # Gah too busy man. One day I'll get back, I have naother 6 hards to catch up on. 


    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        dic = defaultdict(list)
        for i in range(1, n + 1):
            for comb in itertools.combinations(coins, i):
                dic[len(comb)].append(math.lcm(*comb))
        
        def count(dic, target):
            ans = 0
            for i in range(1, n + 1):
                for lcm in dic[i]:
                    ans += target // lcm * pow(-1, i + 1)
            return ans
        
        start, end = min(coins), min(coins) * k
        while start + 1 < end:
            mid = (start + end) // 2
            if count(dic, mid) >= k:
                end = mid
            else:
                start = mid
        if count(dic, start) >= k:
            return start
        else:
            return end
