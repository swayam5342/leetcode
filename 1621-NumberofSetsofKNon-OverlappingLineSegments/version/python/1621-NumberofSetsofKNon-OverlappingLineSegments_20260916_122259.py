# Last updated: 9/16/2026, 12:22:59 PM
1class Solution:
2    def numberOfSets(self, n: int, k: int) -> int:
3        MOD = 10**9 + 7
4
5        fact = [1] * (n + k)
6        for i in range(1, n + k):
7            fact[i] = fact[i - 1] * i % MOD
8
9        inv_fact = [1] * (n + k)
10        inv_fact[-1] = pow(fact[-1], MOD - 2, MOD)
11
12        for i in range(n + k - 1, 0, -1):
13            inv_fact[i - 1] = inv_fact[i] * i % MOD
14
15        r = 2 * k
16        total = n + k - 1
17
18        return (
19            fact[total]
20            * inv_fact[r] % MOD
21            * inv_fact[total - r] % MOD
22        )