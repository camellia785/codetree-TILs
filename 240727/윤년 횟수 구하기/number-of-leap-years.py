n = int(input())
cnt = 0

# 1년부터 n년까지의 윤년의 횟수를 구하기
for i in range(1, n+1):
    if (i % 4 == 0 and i % 100!=0) or i % 400 == 0:
        cnt += 1

print(cnt)