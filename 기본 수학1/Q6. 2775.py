# 오답 (내 답도 맞는데, 시간 초과뜸. (재귀함수로 품))
# total = 0
# def people_num(floor, room):
#     global total
#     people_sum = 0
#     if floor == 0:
#         total += room
#         return total
    
#     for i in range(1,room+1):
#         people_num(floor-1, i)
        
# numTestCases = int(input())
# for i in range(numTestCases):
#     k = int(input())
#     v = int(input())
#     people_num(k,v)
#     print(total)
#     total = 0

# 정답
t = int(input())
for _ in range(t):  
    floor = int(input())  # 층
    num = int(input())  # 호
    f0 = [x for x in range(1, num+1)]  # 0층 리스트
    for k in range(floor):  # 층 수 만큼 반복
        for i in range(1, num):  # 1 ~ n-1까지 (인덱스로 사용)
            f0[i] += f0[i-1]  # 층별 각 호실의 사람 수를 변경
    print(f0[-1])  # 가장 마지막 수 출력