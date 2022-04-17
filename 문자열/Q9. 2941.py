S = input()
cnt = 0
croatia_alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in croatia_alphabet:
    S = S.replace(i,"0")
print(len(S))