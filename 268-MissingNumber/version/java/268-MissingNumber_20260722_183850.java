// Last updated: 7/22/2026, 6:38:50 PM
1class Solution {
2    public int missingNumber(int[] nums) {
3        int n = nums.length;
4
5        int expected = n * (n + 1) / 2;
6
7        int actual = 0;
8        for (int num : nums) {
9            actual += num;
10        }
11
12        return expected - actual;
13    }
14}