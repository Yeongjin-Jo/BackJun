a,b = input().split()
a,b = int(a), int(b)
print('>') if a > b else (print('<') if a < b else( print("==")))