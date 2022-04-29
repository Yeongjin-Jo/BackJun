A,B,C = [int(i) for i in input().split()]

if B >= C :
    units = -1
else:
    units = A // (C-B) + 1
print(units)