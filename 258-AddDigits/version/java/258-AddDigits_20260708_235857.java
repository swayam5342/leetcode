// Last updated: 7/8/2026, 11:58:57 PM
1class Solution {
2    public int addDigits(int num) {
3        while (num>9){
4            num = add(num);
5        }
6        return num;
7    }
8    public int add(int n){
9        int c=0;
10        while (n>0){
11            c+=n%10;
12            n = n/10;
13        }
14        return c;
15    }
16}