# Last updated: 10/2/2026, 6:30:25 AM
1class Solution:
2    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
3
4        if n == 0:
5            return True
6
7        for i in range(len(flowerbed)):
8
9            if flowerbed[i] == 0:
10                left = (i == 0 or flowerbed[i - 1] == 0)
11                right = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
12
13                if left and right:
14                    flowerbed[i] = 1
15                    n -= 1
16
17                    if n == 0:
18                        return True
19
20        return False