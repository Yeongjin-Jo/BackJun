answer = input().split()
A = answer[0]
B = answer[1]

def newStr(data):
    temp = ""
    for i in range(len(data)-1,-1,-1):
        temp += data[i]        
    return temp
A = newStr(A)
B = newStr(B)

if A > B: print(A)
else: print(B)

