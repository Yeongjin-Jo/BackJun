cnt = 0
a = input()
if (int(a) < 10):
    a = '0' + a
a0 = a
while True:
    a = (a[1]) + str(int(a[0])+int(a[1]))[-1]
    cnt += 1
    if (a == a0):
        break
print(cnt)


