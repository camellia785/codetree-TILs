def print_ascending(n):
    if n>0:
        print_ascending(n-1)
        print(n, end=' ')

def print_descending(n):
    if n>0:
        print(n, end=' ')
        print_descending(n-1)

N = int(input())

# 1부터 N까지 차례대로 출력
print_ascending(N)
print()  # 줄바꿈을 위한 출력

# N부터 1까지 차례로 출력
print_descending(N)
print()  # 줄바꿈을 위한 출력