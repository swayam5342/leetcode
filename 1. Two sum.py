def twoSum(nums: list[int], target: int) -> list[int]:
    new_list : list[int] =  []
    new_list.extend(nums)
    point1 = 0
    point2 = len(nums) - 1
    new_list.sort()
    while point1 < point2:
        if new_list[point1] + new_list[point2] > target:
            point2 -=  1
        elif new_list[point1] + new_list[point2] < target:
            point1 += 1
        else:
            return [nums.index(new_list[point1]), nums.index(new_list[point2])]
        
n :list[list[int]] = [[3,3],[3,2,4],[2,3,4]]
tra : int = 6
for i in n:
    print(twoSum(i,tra))