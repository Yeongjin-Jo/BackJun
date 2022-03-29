array = []
for i in range(1,10):
    array.append(int(input()))
max = array[0]
max_index = 0
for i, component in enumerate(array):
    if component >= max:
        max = component
        max_index = i+1
print(f'{max}\n{max_index}')