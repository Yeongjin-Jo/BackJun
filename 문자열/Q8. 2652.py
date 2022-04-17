def alphabetToDigit(alphabet):
    if 80 <= ord(alphabet) <= 83:
        return 7
    elif 84 <= ord(alphabet) <= 86:
        return 8
    elif 87 <= ord(alphabet):
        return 9
    elif ord(alphabet) % 3 == 0:
        result = ord(alphabet) - 66
    elif ord(alphabet) % 3 == 1:
        result = ord(alphabet) - 67
    else:
        result = ord(alphabet) - 65
    return result // 3 + 2

S = input()
time = 0
for i in S:
    time += alphabetToDigit(i) - 1 + 2
print(time)