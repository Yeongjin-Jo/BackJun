def restCal(digit):
    rest = digit % 10
    return rest


def f(digit):
    data = digit
    start = True
    while digit > 0:
        if (start):
            rest = restCal(digit)
            start = False
            digit //= 10
            d = rest - restCal(digit)
        else:
            if (d != rest - restCal(digit)):
                break
            else:
                d = rest - restCal(digit)
                rest = restCal(digit)
                digit //= 10
    else:
        return data

N = int(input())
cnt = 0
for i in range(1,N+1):
    if f(i): cnt += 1
print(cnt)
    
        
        