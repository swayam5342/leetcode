// Last updated: 7/22/2026, 7:15:28 PM
1class Solution {
2    public int countOdds(int low, int high) {
3        if(low%2==0 && high%2==0){
4            return (high-low)/2;
5        }else{
6            return (high-low)/2 +1;
7        }
8    }
9}