digitSize = int(input())
digit_string = int(input())
digit_string = str(digit_string)

def sumCal(digit_string):
    sum = 0
    for i in range(len(digit_string)):
        sum += int(digit_string[i])
    return sum

print(sumCal(digit_string))
