class Solution:
    # Step 1 is going to be solving [pos][length] = isPalindrome
    # Step 2 then becomes a basic DP: Given [ind], try all lengths -> return max
    
    # So the real question is, how can we solve for all palindromes in n^2?
    # The problem is that we need to shift what the prev inds looked at, each expansion
    # Can we instead construct this with (mid, length) iteration? 
    # Thats still n^2 and should be expandable with ease. Yes!

    def searchPalindromeFromMids(self, midLeft, midRight):
        s, n, k, isPalindromeString = self.s, self.n, self.k, self.isPalindromeString
        for dist in range(min(midLeft, n - midRight - 1) + 1):
            left = midLeft - dist
            right = midRight + dist
            if s[left] == s[right]:
                isPalindromeString.add((left, right))
            else:
                break
        
    def maxPalindromes(self, s: str, k: int) -> int:
        # Step 1: Construct isPalindromeString
        isPalindromeString = set() # (start, end) exists -> s[start..end] is palindrome
        n = len(s)
        self.s, self.k, self.n = s, k, n
        self.isPalindromeString = isPalindromeString

        for midPoint in range(len(s)):
            self.searchPalindromeFromMids(midPoint, midPoint)
            if midPoint:
                self.searchPalindromeFromMids(midPoint - 1, midPoint)
        
        # Now step 2 is DP. Since it's 1D, we can just do it in a basic loop
        maxSubarrays = [0 for ind in range(self.n + 1)]
        for ind in range(n - 1, -1, -1):
            maxFound = maxSubarrays[ind + 1] # Skip this ind

            for palindromeEnd in range(ind + k - 1, n):
                if (ind, palindromeEnd) in isPalindromeString:
                    option = 1 + maxSubarrays[palindromeEnd + 1]
                    maxFound = max(maxFound, option)
            
            maxSubarrays[ind] = maxFound
        
        return maxSubarrays[0]

