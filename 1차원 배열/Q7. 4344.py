C = int(input())
for i in range(C):
    mean = 0
    above_mean = 0
    students_and_results = list(map(int, input().split()))
    mean = sum(students_and_results[1:]) / students_and_results[0]
    for m in students_and_results[1:]:
        if m > mean:
            above_mean += 100/(students_and_results[0])
    print(f'{above_mean:.3f}%')