# Last updated: 9/12/2026, 2:58:56 PM
1class NumArray:
2
3    def __init__(self, nums: List[int]):
4        self.prefix = [0]
5
6        for num in nums:
7            self.prefix.append(self.prefix[-1] + num)
8        
9
10    def sumRange(self, left: int, right: int) -> int:
11        return self.prefix[right + 1] - self.prefix[left]
12
13
14# Your NumArray object will be instantiated and called as such:
15# obj = NumArray(nums)
16# param_1 = obj.sumRange(left,right)