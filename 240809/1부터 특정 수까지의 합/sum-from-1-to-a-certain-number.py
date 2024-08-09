def calculate(N):
    cnt = 0
    i = 1
    for i in range(N+1):
        cnt += i
        i = i+1

    return cnt//10

N = int(input())
print(calculate(N))