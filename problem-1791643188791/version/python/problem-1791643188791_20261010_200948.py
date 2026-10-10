# Last updated: 10/10/2026, 8:09:48 PM
1class Solution:
2    def resilientSubarray(self, nums: list[int], k: int) -> int:
3        n,ans, i = len(nums),1,0
4
5        while i < n:
6            r = nums[i] % k
7            j = i
8            while j < n and nums[j] % k == r:
9                j+=1
10
11            m = j -i
12            g = k//gcd(r,k)
13            ans = max(ans,1 + ((m-1)//g)*g)
14            i=j
15        return ans