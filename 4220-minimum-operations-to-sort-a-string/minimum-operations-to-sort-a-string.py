class Solution:
    # For n=2, its just 0 or -1
    # For everything else, we either need 0 (already sorted), 1 (first or last in place), or 2
    # The worst case is to first include the element meant to be first or last, then do the rest
    # So this becomes a trivial check: if first/last already in place, we sort in just 1. Else 2.
    # Edge case: if first and last are swapped, we are forced to take 3. 

    def minOperations(self, s: str) -> int:
        # Basic edge cases
        if len(s) == 1:
            return 0
        elif len(s) == 2:
            if s[0] <= s[1]:
                return 0
            else:
                return -1
        
        # Now general case
        correct = "".join(sorted(list(s)))
        if s == correct:
            return 0
        elif s[0] == correct[0] or s[-1] == correct[-1]:
            return 1
        elif s[0] == correct[-1] and s[-1] == correct[0] and correct[0] != correct[1] and correct[-1] != correct[-2]:
            # first and last are swapped, and no dupes anywhere to get them in place immediately
            return 3
        else:
            return 2
