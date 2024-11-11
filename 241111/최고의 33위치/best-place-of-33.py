N = int(input())
A =[list(map(int, input().split())) for _ in range(N)]

answer = 0
for row in range(1, N-1): # 행마다
    for col in range(1, N-1): #열마다
        cnt = 0
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                cnt += A[r][c]
            answer = max(answer, cnt)


print(answer)