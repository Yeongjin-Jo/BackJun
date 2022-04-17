S = input()

def wordCall(S):
    call_list = []

    start = int(ord("a"))
    for i in range(start, start+26):
        word_call = False
        for word_idx in range(len(S)):
            if i == int(ord(S[word_idx])):
                call_list.append(word_idx)
                word_call = True
                break
        if word_call == False:
            call_list.append(-1)
    return call_list

[print(i, end = " ") for i in wordCall(S)]