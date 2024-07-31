# 1. 입력 받기: 첫 번째 줄에 정수 n이 주어지고, 다음 n개의 줄에 (a, b) 쌍이 주어집니다.
# 2. 곱 계산하기: 각 (a, b) 쌍에 대해 a부터 b까지의 곱을 계산합니다.

n = int(input())

for _ in range(n):
    a,b=map(int, input().split())

    k = 1
    for i in range(a, b+1):
        k *= i

    print(k)