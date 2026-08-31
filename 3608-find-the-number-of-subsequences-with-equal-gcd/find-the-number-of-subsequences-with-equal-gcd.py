class Solution:
    # Well my comments got removed as I was thinking, great.
    # Anyways I had gcd so we'll consider this in the future. 
    # Doing public sol for now to focus on other work
    
    def subsequencePairCount(self, nums: List[int]) -> int:
        @cache
        def dp(i, s1, s2):

            if i >= len(nums):

                if s1 == s2:
                    return 1
                
                return 0
            
            ans = 0
            ans += dp(i + 1, s1, s2)
            
            if s1 == None:
                ans += dp(i + 1, nums[i], s2)
            else:
                ans += dp(i + 1, math.gcd(s1, nums[i]), s2)
            
            if s2 == None:
                ans += dp(i + 1, s1, nums[i])
            else:
                ans += dp(i + 1, s1, math.gcd(s2, nums[i]))


            return ans % (10 ** 9 + 7)

        return (dp(0, None, None) - 1)  % (10 ** 9 + 7)       