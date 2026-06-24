class Solution:
    # Okay, so this takes yesterday's question and flips the constaints.
    # We can't do any DP involving n / ind now, because the length is too long to even do a single one

    # Can we maybe do funny binary splitting for this? So for example n=10^8 is two strings of 10^4
    # So if we then split this into the two layers, we can solve DP(n): {(lastVal, mode) : count} and (firstVal, mode) : Count
    # In this case, 10^9 is immediately split into < 10^5, and that DP is now solvable in range^2.
    # We can actually optimize to just O(range) combination with the prefix sum trick.

    # So we still want to compute per-layer, but we chain layers together by stitching all end/start combos
    # It's hard to prove this complexity here because DP is using (n) but the gaps will be very wide until like n < 100
    # Eg: 10^9 /2 = 500000000 -> /2  another 9 times to get the first split: 976562.5 < 10^6.
    # 976562 and 976563 can then start splitting into 2 at each level, ie log(10^6) = 20. 
    # While each level doubles, once we get to like 10^4 the values consolidate, so we can forget 10^4 and put that as precompute

    # This means the computations would actually be about range * (2 * (10^4.5) / 10^ 3 -> lets say 1000)
    # So like within a million. Should work .. but this is going to be a pain.
    # Gonna just use a public solution cuz I did 4 hards last weekend

        

    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        up = list(range(m))

        T = [[0]*m for _ in range(m)]
        for i in range(1, m):
            for k in range(m - i, m):
                T[i][k] = 1

        def matmul(A, B):
            sz = len(A)
            C = [[0]*sz for _ in range(sz)]
            for i in range(sz):
                for k in range(sz):
                    if not A[i][k]: continue
                    for j in range(sz):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C

        def matpow(M, p):
            sz = len(M)
            res = [[int(i == j) for j in range(sz)] for i in range(sz)]
            while p:
                if p & 1: res = matmul(res, M)
                M = matmul(M, M)
                p >>= 1
            return res

        Tn = matpow(T, n - 2)

        ans = 0
        for i in range(m):
            for j in range(m):
                ans = (ans + Tn[i][j] * up[j]) % MOD

        return ans * 2 % MOD
        