S = input().upper()

dictS = {}

for i in range(len(S)):
    if dictS.get(S[i]) == None:
        dictS[S[i]] = S.count(S[i])
    else:
        continue

listo = []

for i in dictS.keys():
    if dictS[i] == max(dictS.values()):
        listo.append(i)

if len(listo) > 1:print("?")
else:print(listo[0])