def repeatString(repeat, repeat_string):
    for alphabet_idx in range(len(repeat_string)):
        if alphabet_idx == len(repeat_string) - 1: print(repeat_string[alphabet_idx]*repeat)    
        else: print(repeat_string[alphabet_idx]*repeat, end = "")

numTestCases = int(input())
for i in range(numTestCases):
    testCase = input().split()
    repeat = int(testCase[0])
    repeat_string = testCase[1]
    repeatString(repeat, repeat_string)
        