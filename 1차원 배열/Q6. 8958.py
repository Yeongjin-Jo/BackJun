N = int(input())
score_board = []
for i in range(N):
    result = input()
    correct_answer = 0
    score = 0
    for answer in result:
        if answer == 'O':
            correct_answer += 1
            score += correct_answer
        else:
            correct_answer = 0
    score_board.append(score)
for i in score_board:
    print(i)