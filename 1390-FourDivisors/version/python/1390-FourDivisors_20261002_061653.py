# Last updated: 10/2/2026, 6:16:53 AM
1class Solution:
2    def sumFourDivisors(self, nums: list[int]) -> int:
3        total = 0
4
5        for num in nums:
6            count = 0
7            divisor_sum = 0
8
9            for i in range(1, int(num ** 0.5) + 1):
10                if num % i == 0:
11                    count += 1
12                    divisor_sum += i
13                    if i != num // i:
14                        count += 1
15                        divisor_sum += num // i
16
17            if count == 4:
18                total += divisor_sum
19
20        return total