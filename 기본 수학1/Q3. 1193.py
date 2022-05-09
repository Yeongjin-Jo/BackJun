n = 1
k = int(input())
while k > 1 + (n-1)*(n+2)/2:
    n += 1

if n % 2 != 0:
    row = n
    col = 1
    for i in range((n-2)*(n+1)//2+2,(n-1)*(n+2)//2+2):
        if i == k:
            print(str(row)+'/'+str(col))
        else:
            row -= 1
            col += 1
else:
    row = 1
    col = n
    for i in range((n-2)*(n+1)//2+2,(n-1)*(n+2)//2+2):
        if i == k:
            print(str(row)+'/'+str(col))
        else:
            row += 1
            col -= 1