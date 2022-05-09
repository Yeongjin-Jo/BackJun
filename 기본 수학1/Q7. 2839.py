N = int(input())
def num_plastic(N):
    plastic = 0
    temp = N // 5
    for i in range(temp,-1,-1):
        if (N - 5*i) % 3 == 0:
            return i+((N - 5*i) // 3)
    else:
        return -1
print(num_plastic(N))