#public sol, no time. But generally I think the intuitive solution is to convert the array to [num occur, num occur, etc] and then one-pass should work
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7

        def modinv(x):
            return pow(x, MOD - 2, MOD)
        
        # Precompute factorials
        max_n = n
        fact = [1] * (max_n)
        for i in range(1, max_n):
            fact[i] = (fact[i - 1] * i) % MOD
        
        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return (fact[a] * modinv(fact[b]) % MOD) * modinv(fact[a - b]) % MOD

        comb_part = comb(n - 1, k)
        power_part = pow(m - 1, n - 1 - k, MOD)

        return comb_part * m % MOD * power_part % MOD