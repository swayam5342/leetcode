def isPalindrome(x: int) -> bool:
    l : list[int] = list(str(x))
    point1 = 0
    point2= len(l)-1
    while point1 < point2:
        if l[point1] == l[point2]:
            point2 -= 1
            point1 += 1
        else:
            return False
    return True


x = [10,121,-121]
for i in x:
    print(isPalindrome(i))