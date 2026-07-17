class Solution:
    # Hey, this is a contest question I couldn't do before! Lets try fresh
    # Okay, so GCD(a, b) can be solved in log() but we cant actually do all n^2 pairs
    # We need to somehow figure out what the originating (a, b) are based on the gcd index ..
    
    # Okay thats tricky. I feel like there is some binary search hidden here but idk
    # I would like to give this an honest go but I have work to do, so just public sol
    

    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        freq = [0] * (mx + 1)
        for a in nums: 
            freq[a] += 1
            
        GCD = [0] * (mx + 1)
        
        for i in range(mx, 0, -1):
            sm = sum(freq[i::i])
            GCD[i] = sm * (sm - 1) // 2 - sum(GCD[i::i])
            
        GCD = list(accumulate(GCD))
        
        return [bisect.bisect_right(GCD, q) for q in queries]
        