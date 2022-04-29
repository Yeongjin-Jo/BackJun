numTestCases = int(input())
for i in range(numTestCases):
    H, W, N = map(int, input().split())
    
    cnt = 0
    for i in range(1, W+1):
        for j in  range(1, H+1):
            cnt += 1
            if N == cnt:
                print(j*100+i)