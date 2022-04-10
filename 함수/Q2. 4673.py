def d(x):
    sum = 0
    sum += x
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum

for digit in range(1,10000):
    numsize = digit
    digitnum = 0
    while numsize > 0:
        digitnum += 1
        numsize //= 10 
    
    for i in range(1, 9*digitnum+1):
        if d(digit - i) == digit:
            break
    else:
        print(digit)