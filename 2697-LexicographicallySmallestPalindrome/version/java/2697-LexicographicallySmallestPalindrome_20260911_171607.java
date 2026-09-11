// Last updated: 9/11/2026, 5:16:07 PM
1class Solution {
2    public String makeSmallestPalindrome(String s) {
3        char[] arr = s.toCharArray();
4        int l = 0;
5        int r = arr.length - 1;
6        while(l < r){
7            if(arr[l]!=arr[r]){
8                char samll = (char)Math.min(arr[l],arr[r]);
9            arr[r]=samll;
10            arr[l]=samll;
11            }
12            r--;
13            l++;
14        }
15        return new String(arr);
16    }
17}