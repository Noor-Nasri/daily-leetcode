class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # This is not my solution, since mine was the combinatorics approach. This is the expected DP
        # I am submitting to review later. 
        mod=10**9+7
        dp=[0]*(high+1)
        dp[0]=1
        for i in range(1, high+1):
            ans=1
            if i>=zero: ans+=dp[i-zero]
            if i>=one: ans+=dp[i-one]
            dp[i]=ans%mod
        return (dp[high]-dp[low-1]+mod)%mod
        
        