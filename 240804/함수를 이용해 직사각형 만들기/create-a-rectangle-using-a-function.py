def print_rectangle(n, m):
    for i in range(n):
        print('1' * m)

# 입력을 받습니다.
n, m = map(int, input().split())

# 직사각형을 출력하는 함수를 호출합니다.
print_rectangle(n, m)