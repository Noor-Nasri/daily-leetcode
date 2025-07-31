class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # If you expand from x until the point equal to OR(x..end), you found all points that start at X
        # Now to start at x+1, you lose an OR. How do we avoid restarting?

        # Can we do this more like a rolling sequence? Each time we see an element, we consider extending the existing list.
        # So, maintain a "until y" list, then iterate on it. But that is still n^2. How do we instead know what combos are unseen?

        # gotta get to work man, I see this solution which is exactly my idea but I dont understand why its not n^2?
        res = set()
        cur = set()
        
        for num in arr:
            next_cur = {num}
            for prev in cur:
                next_cur.add(prev | num)
            cur = next_cur
            res.update(cur)
        
        return len(res)
        