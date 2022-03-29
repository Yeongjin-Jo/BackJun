N = int(input())
array = list(map(int, input().split()))
min = array[0]
max = array[0]
for i in array:
    if min > i:
        min = i
    if max < i:
        max = i
print(min, max)  
        
    