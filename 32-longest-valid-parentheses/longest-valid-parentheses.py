class Solution:
    # If we have something like ((), we continue expanding but only len=2 is valid. Another ) means len=4.
    # This makes it tricky - we cant just endlessly expand because we might need to shrink.
    # Can this be binary search? Like, if len=4 exists must len=2 always exist?
    # ()() and (()), so yes. For len=8, would len=4 always exist? Yes. Either AB or A inside of B.
    # So this just becomes binary search. Look for len=x with single sweep.

    # But verifying len=x is still tricky, we need to shift windows.
    # I feel like my first greedy plan works. When we see ((), we know its still valid and count ) means len=2.
    # Lol, this is kind of simply then. I overthinked it


    def longestValidParentheses(self, s: str) -> int:
        maxLen = 0
        numPaired = 0
        unpairedInds = []
        for ind in range(len(s)):
            c = s[ind]
            if c == "(":
                unpairedInds.append(ind)
            elif not unpairedInds:
                # No valid seq can include this ind - every open got closed before this.
                numPaired = 0
                unpairedInds = []
            else:
                unpairedInds.pop()
                numPaired += 1
                
                if unpairedInds:
                    validLength = ind - unpairedInds[-1]
                else:
                    validLength = numPaired*2
                    
                maxLen = max(maxLen, validLength)

        return maxLen