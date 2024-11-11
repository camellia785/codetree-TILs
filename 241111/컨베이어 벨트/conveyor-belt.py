# 변수 선언 및 입력
n, t = tuple(map(int, input().split()))
u = list(map(int, input().split()))
d = list(map(int, input().split()))

for _ in range(t):
    # 1. 위에서 > 가장 오른쪽에 있는 숫자를 따로 temp값에 저장
    temp = u[n-1]

    # 2. 위에 있는 숫자들을 완성
    # 오른쪽에서부터 채워넣고, 맨 왼쪽 숫자는 아래에서 가져오기
    for i in range(n-1, 0, -1): # 위쪽 줄의 숫자들을 오른쪽으로 한 칸씩 밀어
        u[i] = u[i-1]
    u[0] = d[n-1] # 위쪽 줄의 맨 첫 번째 칸은 아래쪽 줄의 마지막 숫자로 채워

    # 3. 아래에 있는 숫자들을 완성
    # 오른쪽부터 채워넣기, 맨 왼쪽 숫자는 temp값을 가져오기

    for i in range(n-1, 0, -1): # 아래쪽 줄의 숫자들도 오른쪽으로 한 칸씩 밀어
        d[i] = d[i-1]
    d[0] = temp # 아래쪽 줄의 맨 첫 번째 칸은 위쪽 줄에서 빼놓은 마지막 숫자로 채워

#출력 - 위, 아래 결과
for elem in u:
    print(elem, end=" ")
print()

for elem in d:
    print(elem, end= ' ')