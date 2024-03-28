def removeDuplicates(nums):
    if not nums:
        return 0
    point1 = 0
    for point2 in range(1, len(nums)):
        if nums[point2] != nums[point1]:
            point1 += 1
            nums[point1] = nums[point2]
    return point1 + 1

test: list[list[int]] = [[1,1,2],[0,0,1,1,1,2,2,3,3,4]]

for i in test:
    print(removeDuplicates(i))

