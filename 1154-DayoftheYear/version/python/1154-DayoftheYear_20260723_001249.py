# Last updated: 7/23/2026, 12:12:49 AM
1class Solution:
2    def dayOfYear(self, date: str) -> int:
3        day = {
4            0:0
5            ,1:31
6            ,2:59
7            ,3:90
8            ,4:120
9            ,5:151
10            ,6:181
11            ,7:212
12            ,8:243
13            ,9:273
14            ,10:304
15            ,11:334,
16            12:365
17        }
18        data = date.split("-")
19        y,m,d = int(data[0]),int(data[1]),int(data[2])
20        if ((y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)) and m >2:
21            return day[m-1]+ d +1
22        else:
23            return day[m-1]+d
24
25