def assertgroupWord(S):
    groupWord = ""
    curr = None
    for i in S:
        if curr != i:
            curr = i
            if groupWord.find(curr) != -1:
                return 0
            else:
                groupWord += i
    return 1

numTestCases = int(input())
cnt = 0
for i in range(numTestCases):
    S = input()
    cnt += assertgroupWord(S)
print(cnt)


        