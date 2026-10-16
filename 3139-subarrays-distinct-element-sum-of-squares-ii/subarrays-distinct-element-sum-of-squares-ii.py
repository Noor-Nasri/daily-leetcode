class Solution:
    # We need to solve all subarrays without doing the full n^2.
    # My immediate guess is some sort of tree structure that somehow solves the final val
    # Eg: [0] and [1] leaf nodes are for value (1) and (2), and the parent node maintains count=2
    # But how do you merge nodes or update parent without a full O(n)?

    # Values go until 10^5 so we cant do a hash-based trick. 
    # Can we consider the full array, and somehow exclude left or right without care?
    # Eg: If element [0] is the only 1, we just add onto all subarrays including element [1]
    # If [0] occurs again at [4], then we add onto all counts found in 1->3.
    
    # Can we do some form of divide and conquer? Solve (left) + Solve (right) + Solve(intersect)
    # To solve intersect, we expand on both sides in O(n) and somehow multiply them together?
    # I think this is the way, but solving the intersection needs to be fleshed out.

    # I can't figure out how we can sweep the intersection in O(n)
    # Will do publis sol again cuz I am busy .. I will need to revisit this eventually
    
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        size = 4 * n

        sum1 = [0] * size
        sum2 = [0] * size
        lazy = [0] * size

        def apply(node, l, r, val):
            length = r - l + 1
            sum2[node] = (
                sum2[node]
                + 2 * val * sum1[node]
                + length * val * val
            ) % MOD
            sum1[node] = (
                sum1[node] + length * val
            ) % MOD
            lazy[node] += val

        def push(node, l, r):
            if lazy[node]:
                mid = (l + r) // 2
                apply(node * 2, l, mid, lazy[node])
                apply(node * 2 + 1, mid + 1, r, lazy[node])
                lazy[node] = 0

        def update(node, l, r, ql, qr, val):
            if ql <= l and r <= qr:
                apply(node, l, r, val)
                return

            push(node, l, r)
            mid = (l + r) // 2

            if ql <= mid:
                update(node * 2, l, mid, ql, qr, val)
            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr, val)

            sum1[node] = (
                sum1[node * 2] + sum1[node * 2 + 1]
            ) % MOD
            sum2[node] = (
                sum2[node * 2] + sum2[node * 2 + 1]
            ) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            p = last.get(x, -1)
            update(1, 0, n - 1, p + 1, i, 1)
            last[x] = i
            ans = (ans + sum2[1]) % MOD

        return ans