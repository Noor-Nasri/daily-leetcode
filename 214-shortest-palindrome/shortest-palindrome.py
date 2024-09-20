class Solution:
    '''
    def isPalindrome(self, s, ind1, ind2):
        if (ind1, ind2) in self.knownPalindromes:
            return self.knownPalindromes[(ind1, ind2)]

        ans = False
        if ind1 == ind2: 
            ans = True
        elif s[ind1] != s[ind2]: 
            ans = False
        elif ind1 + 1 == ind2:  
            ans = True
        else:
            ans = self.isPalindrome(s, ind1 + 1, ind2 - 1)
            del self.knownPalindromes[(ind1 + 1, ind2 - 1)] # dont need old memory anymore
        
        self.knownPalindromes[(ind1, ind2)] = ans
        return self.knownPalindromes[(ind1, ind2)]
    '''
    def shortestPalindrome(self, s: str) -> str:
        # First, we solve for the longest palindrome including starting character
        # Then we can simple duplicate the remaining characters to make smallest full palindrome
        # We can build up the palindrome length one at a time by checking [first] == [last] and palindrome(mid)

        if len(s) < 2: return s

        '''self.knownPalindromes = { (0, 0) : True }
        longestPalindrome = 1

        for ind_end in range(1, len(s)):
            if self.isPalindrome(s, 0, ind_end):
                longestPalindrome = ind_end + 1
            
            # Update [1, x] so that next iteration can also check in O(1)
            #self.isPalindrome(s, 1, ind_end)

        if longestPalindrome == len(s):
            return s
        
        return s[longestPalindrome:][::-1] + s
        '''

        for ind_end in range(len(s), -1, -1):
            sub = s[:ind_end]
            if sub == sub[::-1]:
                return s[ind_end:][::-1] + s


        