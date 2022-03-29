array = []
result = 1
cnt_array = [0,0,0,0,0,0,0,0,0,0]
for i in range(3):
    result *= int(input())
for i in range(10):
    for j in str(result):
        if str(i) == j:
            cnt_array[i] += 1
for i in cnt_array:
    print(i)