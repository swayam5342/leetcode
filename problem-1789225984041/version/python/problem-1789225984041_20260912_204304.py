# Last updated: 9/12/2026, 8:43:04 PM
1import bisect
2class Solution:
3    def distantSubarrays(self, nums: list[int], goal: int, k: int) -> int:
4        n = len(nums)
5        p = [0]*(n+1)
6
7        for i in range(n):
8            p[i+1] = p[i] + nums[i]
9
10        l = [0]*(n+1)
11        r = [0]*(n+1)
12
13        for j in range(1,n+1):
14            l[j] = p[j] - goal -k
15            r[j] = p[j] - goal +k
16
17        allv = set(p)
18
19        for j in range(1,n+1):
20            allv.add(l[j])
21            allv.add(r[j])
22
23        sor = sorted(allv)
24        comp = {v:i+1 for i,v in enumerate(sor)}
25        size = len(sor)
26        fenwick = [0]*(size+1)
27        def update(i):
28            while i<=size:
29                fenwick[i] +=1
30                i+=i&(-i)
31
32        def query(i):
33            s=0
34            while i>0:
35                s+= fenwick[i]
36                i-= i&(-i)
37            return s
38
39        update(comp[p[0]])
40        not_dis =0
41        for j in range(1,n+1):
42            lj,rj = l[j],r[j]
43            if lj < rj:
44                cnt_less_r = query(comp[rj]-1)
45                cnt_leq_l = query(comp[lj])
46                not_dis += cnt_less_r - cnt_leq_l
47            update(comp[p[j]])
48
49        total = n*(n+1) // 2
50        return total - not_dis