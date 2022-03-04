H, M = input().split()
H, M = int(H), int(M)

if M < 45:
    H -= 1
    M += 15
else:
    M -= 45
if H < 0:
    H = 23
print(H, M)

print(-45 % 60)
