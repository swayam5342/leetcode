def longestCommonPrefix(strs: list[str]) -> str:
    length = len(strs)
    i = 0
    min_length = float('inf')
    for j in strs:
        if len(j) < min_length:
            min_length = len(j)
    while i < min_length:
        for j in strs:
            if j[i] != strs[0][i]:
                return  j[:i]
        i +=1
    return  strs[0][:i]


n :list[list[str]] = [["flower","flow","flight"],["dog","racecar","car"],["flower"]]
for i in n:
    print(longestCommonPrefix(i))